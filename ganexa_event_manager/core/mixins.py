class AuditableAdminMixin:
    readonly_fields = ('created_by', 'modified_by')

    def save_model(self, request, obj, form, change):
        if obj.pk:
            obj.modified_by = request.user
        else:
            obj.created_by = request.user
        super(AuditableAdminMixin, self).save_model(request, obj, form, change)
