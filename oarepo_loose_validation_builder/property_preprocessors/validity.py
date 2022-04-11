from oarepo_model_builder.builders.jsonschema import JSONSchemaBuilder
from oarepo_model_builder.builders.mapping import MappingBuilder
from oarepo_model_builder.invenio.invenio_record_schema import InvenioRecordSchemaBuilder
from oarepo_model_builder.property_preprocessors import PropertyPreprocessor, process
from oarepo_model_builder.stack import ModelBuilderStack
from oarepo_model_builder.utils.deepmerge import deepmerge


class ValidityPreprocessor(PropertyPreprocessor):


    @process(
        model_builder=JSONSchemaBuilder,
        path="**/properties/*",
        # condition=lambda current, stack: current.type != "xy",
    )
    def modify_fulltext_schema(self, data, stack: ModelBuilderStack, **kwargs):
        try:
            if 'required' in data:
                data.pop('required')
            if 'minLength' in data:
                data.pop('minLength')
            if 'maxLength' in data:
                data.pop('maxLength')
            if 'minimum' in data:
                data.pop('minimum')
            if 'maximum' in data:
                data.pop('maximum')
            if 'exclusiveMinimum' in data:
                data.pop('exclusiveMinimum')
            if 'exclusiveMaximum' in data:
                data.pop('exclusiveMaximum')
            if 'enum' in data:
                data.pop('enum')
                data['oarepo:jsonschema'].pop('enum')
            if 'minContains' in data:
                data.pop('minContains')
            if 'maxContains' in data:
                data.pop('maxContains')
        except:
            pass
        return data


    @process(
        model_builder=InvenioRecordSchemaBuilder,
        path="**/properties/*",
    )
    def modify_fulltext_marshmallow(self, data, stack: ModelBuilderStack, **kwargs):

        return data
