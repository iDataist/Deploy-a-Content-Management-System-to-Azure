# VM vs App Service

## Analyze, choose, and justify the appropriate resource option for deploying the app.


|              | Virtual Machines (VMs)                                                                                                                                                                                                          | App Service                                                                                                                                                                                                                                                                                                       |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cost         | Lower up-front cost compared to purchasing and maintaining hardware.                                                                                                                                                           | Less expensive than VM. You can set the amount of hardware allocated to host your application, and cost varies based on the plan you choose. There are three different tiers - Dev/Test, Production, and Isolated. You’re always paying for the service plan, even if your services or application isn’t running. |
| Scalability  | There are two options when it comes to scaling—Virtual Machine Scale Sets and Load Balancers.                                                                                                                                  | Vertical or Horizontal scaling. Vertical scaling increases or decreases resources allocated to our App Service, such as the amount of vCPUs or RAM, by changing the App Service pricing tier. Horizontal scaling increases or decreases the number of Virtual Machine instances our App Service is running.       |
| Availability | Multiple types to choose from, such as compute or memory-optimized VMs, along with varying amounts of CPU, RAM and storage. Multiple VMs can be grouped to provide high availability.                                          | High availability.                                                                                                                                                                                                                                                                                                |
| Access       | VMs allow you full access and control of the OS (Linux and Windows) and software installed. VMs allow for the installation of custom images and are an excellent choice for migrating from an on-premises server to the cloud. | You have limited access to the host server, so you are unable to control the underlying OS or install software on the server. There are hardware limitations, such as a maximum of 14GB of memory and 4 vCPU cores per instance.                                                                                  |
| Workflow     | They can be more time consuming for the developer than other compute options.                                                                                                                                                  | Continuous deployment model using GitHub, Azure DevOps, or any Git repo.                                                                                                                                                                                                                                          |

In the current situation, an App Service likely works fine. It can scale vertically to meet different demand levels, and the compute resources needed are well within App Service limits.

## Assess app changes that would change your decision.
Virtual Machines may be necessary in the near future if:

- Many more features are added and the web app exceeds the hardware limitations of App Service (14GB of memory and 4 vCPU cores per instance).

- There is a massive increase in the number of users.

- The company needs increased level of control over the underlying OS and meets higher security requirements.


