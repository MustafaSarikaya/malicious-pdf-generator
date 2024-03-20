from javascript import require
import const


def obfuscated_code(js_code):
    """
    Obfuscates JavaScript code using various techniques.

    Parameters:
        js_code (str): The JavaScript code to obfuscate.

    Returns:
        str: The obfuscated JavaScript code.

    Note:
        Requires the javascript-obfuscator module.

    """
    # Require the javascript-obfuscator module
    java_script_obfuscator = require(const.JS_OBFUSCATOR_LIBRARY)

    obfuscation_result = java_script_obfuscator.obfuscate(js_code, {
        'compact': False,
        'controlFlowFlattening': True,
        'controlFlowFlatteningThreshold': 1,
        'numbersToExpressions': True,
        'simplify': True,
        'stringArrayShuffle': True,
        'splitStrings': True,
        'stringArrayThreshold': 1
    })

    print(f"JavaScript code obfuscated.")

    return obfuscation_result.getObfuscatedCode()



