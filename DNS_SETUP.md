# DNS Configuration for www.thinking-peak.com

## GitHub Pages DNS Setup

To make `www.thinking-peak.com` point to your GitHub Pages site, you need to configure the following DNS records at your domain registrar.

### Option 1: CNAME Record (Recommended for www subdomain)

Add the following DNS record:

| Type  | Host/Name | Value/Points to              | TTL  |
|-------|-----------|------------------------------|------|
| CNAME | www       | 08madison.github.io          | 3600 |

### Option 2: A Records (for apex domain thinking-peak.com)

If you also want `thinking-peak.com` (without www) to work, add these A records:

| Type | Host/Name | Value/Points to | TTL  |
|------|-----------|-----------------|------|
| A    | @         | 185.199.108.153 | 3600 |
| A    | @         | 185.199.109.153 | 3600 |
| A    | @         | 185.199.110.153 | 3600 |
| A    | @         | 185.199.111.153 | 3600 |

### GitHub Pages Information

- **Repository**: https://github.com/08madison/thinking-peak
- **GitHub Pages URL**: https://08madison.github.io/thinking-peak/
- **Custom Domain**: www.thinking-peak.com
- **CNAME file**: Already configured in repository

### After DNS Propagation

Once DNS propagates (usually 24-48 hours), your website will be accessible at:
- http://www.thinking-peak.com
- https://www.thinking-peak.com (after enabling HTTPS in GitHub Pages settings)

### Enable HTTPS

After DNS propagates, go to:
1. https://github.com/08madison/thinking-peak/settings/pages
2. Check "Enforce HTTPS" checkbox

This will enable SSL/TLS for your custom domain.
