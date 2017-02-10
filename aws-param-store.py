from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.lookup import LookupBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()

class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):

        try:
            import boto3
        except ImportError:
            raise AnsibleError('Encountered exception while importing boto3')
        client = boto3.client('ssm')

        try:
            decrypt = kwargs['decrypt']
        except KeyError:
            display.vvvv("No decryption option specified, defaulting to False")
            decrypt = False


        ret = []
        for term in terms:
            display.vvvv("Retrieving %s from EC2 Parameter Store" % term)
            try:
                response = client.get_parameters(
                    Names=[
                        term,
                    ],
                    WithDecryption=decrypt
                )
                if len(response['InvalidParameters']) > 0:
                    raise AnsibleError('Invalid parameter')
                else:
                    val = response['Parameters'][0]['Value']
            except Exception as e:
                raise AnsibleError('Encountered exception
                # Check SSM parameter store here
            except Exception as e:
                raise AnsibleError('Encountered exception while fetching {0}: {1}'.format(term, e.message))
            ret.append(val)

        return ret
