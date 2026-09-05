#!/usr/bin/env bash
# ERPNext Installation Script for PetFactory Morocco
# Target: Ubuntu 22.04 LTS server
# Usage: sudo bash setup_erpnext.sh

set -euo pipefail

ERPNEXT_VERSION="version-15"
SITE_NAME="erp.petfactory.ma"
DB_ROOT_PASSWORD="changeme_root_$(openssl rand -hex 8)"
ADMIN_PASSWORD="changeme_admin_$(openssl rand -hex 8)"

echo "=============================================="
echo " ERPNext Installation — PetFactory Morocco"
echo " Version: $ERPNEXT_VERSION"
echo " Site:    $SITE_NAME"
echo "=============================================="

# --- Prerequisites ---
echo "[1/8] Installing system dependencies..."
apt-get update -qq
apt-get install -y -qq \
    python3-dev python3-pip python3-venv \
    redis-server \
    mariadb-server mariadb-client \
    nginx \
    supervisor \
    git curl wget \
    xvfb libfontconfig wkhtmltopdf \
    nodejs npm

# Node.js 18 via nvm if needed
if ! node -v 2>/dev/null | grep -q "v18\|v20"; then
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
fi

npm install -g yarn

# --- MariaDB Configuration ---
echo "[2/8] Configuring MariaDB..."
cat > /etc/mysql/mariadb.conf.d/99-erpnext.cnf <<'EOF'
[mysqld]
innodb-file-format=barracuda
innodb-file-per-table=1
innodb-large-prefix=1
character-set-client-handshake=FALSE
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci

[mysql]
default-character-set=utf8mb4
EOF

systemctl restart mariadb
mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '${DB_ROOT_PASSWORD}';"

# --- Frappe Bench ---
echo "[3/8] Installing Frappe Bench..."
pip3 install frappe-bench

# --- Create bench ---
echo "[4/8] Initializing bench..."
useradd -m -s /bin/bash frappe 2>/dev/null || true
su - frappe -c "
    bench init --frappe-branch ${ERPNEXT_VERSION} frappe-bench
    cd frappe-bench
    bench get-app erpnext --branch ${ERPNEXT_VERSION}
"

# --- Create site ---
echo "[5/8] Creating site: ${SITE_NAME}..."
su - frappe -c "
    cd frappe-bench
    bench new-site ${SITE_NAME} \
        --db-root-password '${DB_ROOT_PASSWORD}' \
        --admin-password '${ADMIN_PASSWORD}' \
        --install-app erpnext
    bench --site ${SITE_NAME} set-config developer_mode 0
    bench use ${SITE_NAME}
"

# --- Production setup ---
echo "[6/8] Setting up production mode..."
su - frappe -c "
    cd frappe-bench
    sudo bench setup production frappe
    bench setup nginx
"
ln -sf /home/frappe/frappe-bench/config/nginx.conf /etc/nginx/conf.d/frappe.conf
systemctl reload nginx

# --- Enable scheduler ---
echo "[7/8] Enabling scheduler..."
su - frappe -c "
    cd frappe-bench
    bench --site ${SITE_NAME} enable-scheduler
"

# --- Print credentials ---
echo "[8/8] Installation complete!"
echo ""
echo "=============================================="
echo " ERPNext is ready"
echo "=============================================="
echo " URL:            https://${SITE_NAME}"
echo " Admin user:     Administrator"
echo " Admin password: ${ADMIN_PASSWORD}"
echo " DB root pass:   ${DB_ROOT_PASSWORD}"
echo ""
echo " IMPORTANT: Save these credentials securely!"
echo " Change passwords after first login."
echo "=============================================="
echo ""
echo " Next: Run the setup wizard at https://${SITE_NAME}"
echo "   - Company: PetFactory Maroc SARL"
echo "   - Country: Morocco"
echo "   - Currency: MAD"
echo "   - Chart of Accounts: Standard (Morocco)"
echo "   - Language: French"
echo "=============================================="
