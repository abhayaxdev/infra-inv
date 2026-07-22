# InfraInv MVP (Phase 0.0)

## Objective:
    We're building an application to store deployment information of ongoing software projects so that all parties involved (stakeholders, QA, Devs, POs, Leadership) can access it on demand without having to reach out to a middleman.
    
    This would include all environments (DEV, STAGING, UAT, PRODUCTION), various user roles and credentials associated with these environments(apps not the server), server address, service details, application status but not server keys.

    Ofcourse, we're going to enforce RBAC in order to ensure permissions based access.

## TODO:

**Here are some guidelines that are a must-follow for the agent:**
    1. Inherit all the models from core.models.BaseModel
    2. All the models should be registered in admin, and fields such as boolean flags and charfields, emailfields should be editable on the list page. Infact, lea
    3. After completing each task, ensure to add a checkmark inside the square brackets [] at the end of each task that says '[x]Done'. This will signal task completion to the engineer.
    4. Agent can also add 'Agent Notes' after [x]Done. This will hold any remarks or design choices the agent had to make by themselves that may have not been defined by the engineer.


**The following tasks are for the agent to write:**

### Model Definition:

Define the following models. If you find that the apps have not been added, you can run the appropriate django command to create an app and register it in INSTALLED_APPS.

*organizations/models.py*

Organization
    - Inherits from core.models.BaseModel
    - Fields will be Name of Org, email_contact(null, blank), website_url(null, blank), email_suffix(null, blank)
    
    [x]Done

Project
    - a field 'organization' will have a FK relationship with Organization
    - and a title field

    [x]Done

Deploy
    - a field 'project' with with FK relationship with Project
    - a field environment=EnvironmentChoices(DEV, STAGING, UAT, PROD)
    - an is_active flag to indicate current status of the deployment, keep default as false.

    [x]Done

DemoCredentials -> this doesn not store server keys, but demo credentials for the various deployed apps
    - a field with FK relationship to Deploy
    - store usernames, password and user roles in standalone fields, 
    - ensure that password field can store encrypted items

    [x]Done

*users/models.py*
CustomUserModel: 
    - Inherits from AbstractUser and core.models.BaseModel
    - For now, we will just have the email field as the unique identifier
    - We'll also have a new field "role" (null=True, blank=False) with choices as follows: STAKEHOLDER, PRODUCT, DEV, INFRA, QA.
    - a field 'organization' will have a FK relationship with Organization

    [x]Done

*users/manager.py*
Before the CustomUser model, create a users/manager.py and create a custom manager to create users, super user based on the CustomUserModel

    [x]Done

*servers/models.py*
ServerDetails:
    - a field to maintain a FK relationship with organization.Deploy
    - fields to store the IP address, services used

    [x]Done


### CRUD
- Since only the superadmin, staff, or users with a certain role (likely infra) and permissions will be doing the CREATING, DELETING, and UPDATING part. For now, we'll use the django admins for it. So just register all the models in admin. Customize the admin cruds as defined in the guidelines above.

    [x]Done

- However, for READ part, since all users should be able to read and interact with the model objects, we'll need a custom user-facing frontend. We'll work on it in the next phase, along with custom permissions and RBAC.

### Frontend
- Build a beautiful looking landing page titled InfraInv with a coming soon, use TemplateView and define it in project/urls.py. I just want to avoid the existing django default template. For this i give you 100% freedom to be as creative as you can. **Impress me!** 
- Take https://nextjs.org/, https://resend.com/, https://alpinejs.dev/, any one of these for design reference. Use them for getting inspiration for the them (typography, colors), no need to copy the entire sitemap end to end.

    [x]Done