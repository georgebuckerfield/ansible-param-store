from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        ret = []

        for term in terms:
            try:
                # Check SSM parameter store here
            except Exception as e:
                raise AnsibleError('Encountered exception while fetching {0}: {1}'.format(term, e.message))
            ret.append(val)

        return ret
