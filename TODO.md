1. Switch from PIP to either poetry or uv
2. Look into dockerization
3. Look into segmenting settings into base, local and prod in order to maintain SOC (Separation of concerns)


### Refactors for Abhaya, not the Agent
[] Review and Rename models and model_fields from organization/models.py. they could be much clearer and precise in terms of intent.
[] Add a phone number field in CustomUserModel, could come in handy if OTPs are introduced to protect organization.models.Credential.password
[] Review model relationships, i think a review is needed sooner rather than later.
[] there is no need for 'is_active' field in organization.models.Deploy model, is_obsolete from BaseModel should be enough. so it can be removed.