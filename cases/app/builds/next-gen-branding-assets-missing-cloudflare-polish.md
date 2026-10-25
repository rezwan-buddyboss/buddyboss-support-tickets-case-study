---
title: Next Gen app icons or splash screen missing after build, Cloudflare Polish converts PNG to WebP
type: app
area: builds
tickets: sample
error: ""
version: ""
applies_to: next gen
keywords: app icon missing, splash screen wrong, branding assets, next gen build, cloudflare polish, webp
---
## Short description
Next Gen build completes but the app icon or splash assets are missing or wrong.

## Symptoms
Build succeeds, but the icons or splash screen in the app are missing or not the uploaded images. The images look correct in the WordPress media library.

## Debugging steps followed
The build log showed nothing useful and the plugin version was current. Checked whether the site sits behind Cloudflare, then checked Cloudflare Speed settings for Polish.

## How it was solved
Disabled Cloudflare Polish for the site, or excluded the branding assets path, then started a new build.

## Root cause or workaround
Cloudflare Polish silently serves PNG files as WebP, and the build pipeline receives the converted file.

## How to recognize it next time
Branding assets wrong on a Next Gen build, the site is on Cloudflare, and the build log is clean. Check Polish first, it takes two minutes.

## What looked like the cause but wasn't
The build log and version drift. The log shows nothing useful and the images look correct in the media library, so checking them first costs a day.
