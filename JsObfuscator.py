from javascript import require
import const


def obfuscated_code(js_code):
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


