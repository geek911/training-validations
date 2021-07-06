from edc_constants.constants import OTHER
from edc_form_validators import FormValidator


class EducationQuestionnaireFormValidator(FormValidator):

    def clean(self):
        self.required_if(
            OTHER,
            field='is_subject_literate',
            field_required='is_literate_witness_available'
        )
