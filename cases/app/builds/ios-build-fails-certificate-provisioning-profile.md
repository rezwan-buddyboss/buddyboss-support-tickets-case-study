---
title: iOS build fails with E016 or E017 certificate and provisioning profile error
type: app
area: builds
tickets: sample
error: "E016, E017"
version: ""
applies_to: classic, next gen
keywords: ios build failed, E016, E017, distribution certificate, provisioning profile expired, regenerate certificate
---
## Short description
iOS build fails naming a missing distribution certificate or an expired provisioning profile, and regenerating once does not help.

## Symptoms
The build fails with E016 or E017. The customer has often already regenerated the certificate and the build failed again.

## Debugging steps followed
Read the exact code in the AppCenter build log. Checked the provisioning profile expiry in the Apple Developer portal. Confirmed that only one of the two had been regenerated earlier.

## How it was solved
In the iOS build settings: untick generate for both certificate and profile, save, delete both with the cross, save, tick both again, save, then start a new build.

## Root cause or workaround
Certificate and provisioning profile have to be regenerated together. Resetting only the profile leaves the stale certificate in place, so the next build fails the same way.

## How to recognize it next time
E016 or E017 in the build log, especially when the customer says they already regenerated once.

## What looked like the cause but wasn't
Regenerating the certificate or the profile on its own. It looks like the right fix and fails again, because the stale half stays in place.
