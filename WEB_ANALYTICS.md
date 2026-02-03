# Vercel Web Analytics Implementation

This document describes the Vercel Web Analytics implementation for the Buttey Queen Assistant Telegram Bot project.

## Overview

This project now includes a web landing page with Vercel Web Analytics tracking enabled. The landing page serves as a public-facing website for the Telegram bot.

## Implementation Details

### Files Created

1. **`public/index.html`** - Landing page for the bot with analytics tracking
2. **`vercel.json`** - Vercel deployment configuration
3. **`WEB_ANALYTICS.md`** - This documentation file

### Analytics Integration

The analytics script has been added to the landing page using the HTML implementation method:

```html
<!-- Vercel Web Analytics -->
<script>
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

This implementation:
- Uses the plain HTML method (no package installation needed)
- Tracks page views automatically
- Loads asynchronously to avoid blocking page rendering
- Works without a JavaScript framework

## Deployment Instructions

### 1. Enable Web Analytics in Vercel

1. Go to your [Vercel dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click the **Analytics** tab
4. Click **Enable** from the dialog

### 2. Deploy to Vercel

You can deploy using the Vercel CLI or by connecting your Git repository:

#### Option A: Using Vercel CLI

```bash
# Install Vercel CLI if you haven't already
npm i -g vercel

# Deploy to production
vercel --prod
```

#### Option B: Connect Git Repository (Recommended)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Import your GitHub repository
3. Vercel will automatically detect the configuration
4. Click **Deploy**

Future commits to the main branch will automatically deploy.

### 3. Verify Analytics

After deployment:

1. Visit your deployed website
2. Open browser Developer Tools (F12)
3. Check the Network tab for a request to `/_vercel/insights/view`
4. If you see this request, analytics is working correctly

### 4. View Analytics Data

1. Go to your [Vercel dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click the **Analytics** tab
4. After a few hours of traffic, you'll see visitor data

## Features

The landing page includes:

- **Responsive Design** - Works on mobile, tablet, and desktop
- **Modern UI** - Beautiful gradient background and glassmorphism effects
- **Bot Information** - Features, rules, and contact information
- **SEO Optimized** - Proper meta tags for search engines
- **Analytics Tracking** - Automatic visitor tracking via Vercel Web Analytics

## Notes

- The HTML implementation doesn't require the `@vercel/analytics` package
- Page view tracking is automatic
- No route tracking is available with the HTML implementation
- The landing page is separate from the Python bot functionality
- Both can be deployed to Vercel simultaneously

## Bot Deployment

The Python Telegram bot (`main.py`) continues to work independently. The landing page is just a web presence for the project. The bot can be deployed using:

- Heroku (using the existing `Procfile`)
- Any Python hosting service
- A separate server

The web landing page and bot can run on different services if needed.

## Customization

To customize the landing page:

1. Edit `public/index.html`
2. Modify the content, styling, or features
3. Commit and push changes
4. Vercel will automatically redeploy

## Support

For issues or questions:
- Bot Owner: @XEROX_MOD on Telegram
- Vercel Analytics Docs: https://vercel.com/docs/analytics
- Vercel Support: https://vercel.com/support
