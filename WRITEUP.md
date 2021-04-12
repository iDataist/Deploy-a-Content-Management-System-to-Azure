# Write-up Template

## Analyze, choose, and justify the appropriate resource option for deploying the app.
In the current situation, an App Service likely works fine. It can scale vertically to meet different demand levels, and the compute resources needed are well within App Service limits.

### Assess app changes that would change your decision.
There's some consideration that Virtual Machines may be necessary in the near future if many more features are added, or demand changes in a way that requires vertical scaling.  I'd want to know what level of control we need over the underlying OS, and security requirements.
