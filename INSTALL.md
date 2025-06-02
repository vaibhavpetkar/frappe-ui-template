# Installation Guide for Frappe UI Template

This guide will help you install the custom UI template for Frappe ERPNext that mimics the design of https://kymysrwf.manus.space/ while preserving all backend field linkages and logic.

## Prerequisites

- A working Frappe/ERPNext installation
- Frappe bench environment set up

## Installation Steps

1. Navigate to your bench directory:
   ```
   cd path/to/your/frappe-bench
   ```

2. Get the app from GitHub:
   ```
   bench get-app https://github.com/your-username/frappe-ui-template
   ```

3. Install the app on your site:
   ```
   bench --site your-site.local install-app frappe_ui_template
   ```

4. Build assets and restart:
   ```
   bench build
   bench restart
   ```

## Manual Installation (Alternative)

If you prefer to install manually:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/frappe-ui-template apps/frappe_ui_template
   ```

2. Install dependencies:
   ```
   cd apps/frappe_ui_template
   pip install -e .
   ```

3. Install the app on your site:
   ```
   bench --site your-site.local install-app frappe_ui_template
   ```

## Customization

You can customize the template by modifying the following files:

- CSS: `frappe_ui_template/public/css/custom_theme.css`
- JavaScript: `frappe_ui_template/public/js/custom_theme.js`
- Templates: `frappe_ui_template/templates/`

## Troubleshooting

If you encounter any issues during installation:

1. Check the Frappe error logs:
   ```
   bench --site your-site.local show-logs
   ```

2. Ensure all dependencies are installed:
   ```
   bench pip install -r apps/frappe_ui_template/requirements.txt
   ```

3. Clear cache and rebuild:
   ```
   bench --site your-site.local clear-cache
   bench build
   ```

## Support

For any questions or support, please open an issue on the GitHub repository.
