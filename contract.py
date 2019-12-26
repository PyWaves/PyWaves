import requests
import pywaves as pw

class Contract(object):

    def __init__(self, contractAddress, seed):
        self.contractAddress = contractAddress

        metaInfo = self.parseContractAddress()
        extractedMethods = metaInfo.keys()
        for method in extractedMethods:
            signature = self.generateCode(method, metaInfo[method], seed)
            exec(signature, globals())
            setattr(self, method, eval(method))


    def parseContractAddress(self):
        metaInfo = requests.get(pw.NODE + '/addresses/scriptInfo/' + self.contractAddress + '/meta').json()

        return metaInfo['meta']['callableFuncTypes']

    def generateCode(self, method, parameters, seed):
        parameterList = ''
        callParameters = 'parameters = [\n'

        for parameter in parameters.keys():
            parameterList += parameter + ', '
            type = parameters[parameter]

            if type == 'Int':
                callParameters += '\t\t{ "type": "integer", "value": ' + parameter + ' },\n'
            elif type == 'String':
                callParameters += '\t\t{ "type": "string", "value": ' + parameter + ' },\n'
            elif type == 'Boolean':
                callParameters += '\t\t{ "type": "boolean", "value": ' + parameter + ' },\n'

        if len(parameters.keys()) > 0:
            callParameters = callParameters[0:len(callParameters) - 2] + '\n'
        callParameters += '\t]'
        call = 'pw.Address(seed = \'' + seed + '\').invokeScript(\'' + self.contractAddress + '\', \'' + method + '\', parameters, [])'

        code = 'def ' + method + '(' + parameterList[0: len(parameterList) - 2] + '):\n\t' + callParameters + '\n\t' + call

        return code
