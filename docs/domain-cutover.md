# Connect umutyuksel.net — only after reviewing the replacement

The prepared repository does not perform these steps. The old Squarespace site and domain remain unchanged.

1. Publish and review https://umuttolo.github.io using the README instructions. Confirm all pages, mobile layout and PDFs.
2. Save a copy of your existing DNS records. Keep domain registration, email (MX/TXT), verification and other unrelated records intact. Keep the Squarespace website subscription active.
3. Verify your custom domain with GitHub in your account's **Settings → Pages**, following GitHub's current instructions. Add the requested verification TXT record at the domain's DNS provider. Do not remove that verification record later.
4. In the repository's **Settings → Pages**, set **Custom domain** to `umutyuksel.net`. With the supplied custom Actions build, no `CNAME` file is required by GitHub. Set `url: "https://umutyuksel.net"` in `_config.yml` and push the change so canonical/social/sitemap URLs match.
5. At your domain's DNS provider, replace the Squarespace website-routing records with the apex and `www` records specified in the **current GitHub documentation**. The target for `www` is `umuttolo.github.io`, without a scheme or path. Follow GitHub's documented A/AAAA or ALIAS/ANAME options for the apex. Remove only conflicting website-routing records; preserve mail and unrelated records.
6. Wait for GitHub's DNS check and HTTPS certificate to succeed, enable **Enforce HTTPS**, and verify both https://umutyuksel.net and https://www.umutyuksel.net on several devices. Check that one redirects to the chosen canonical hostname, and that email still works.
7. After successful verification and a period of overlap, decide separately whether to cancel Squarespace website hosting. Retain the domain registration and any services you still use. No cancellation is necessary to review or publish the GitHub preview.

For rollback, restore the saved Squarespace routing records at your DNS provider; keep the old website available until the migration is settled. DNS changes can take time to propagate.

Use GitHub's authoritative instructions at cutover time rather than copying potentially stale IP addresses:

- [Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site)
- [Verifying a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages)
- [Securing a Pages site with HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https)
