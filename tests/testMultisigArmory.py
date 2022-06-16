"""
*******************************************************************************    
*   BTChip Bitcoin Hardware Wallet Python API
*   (c) 2014 BTChip - 1BTChip7VfTnrPra5jqci7ejnMguuHogTn
*   
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
*   Unless required by applicable law or agreed to in writing, software
*   distributed under the License is distributed on an "AS IS" BASIS,
*   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*   limitations under the License.
********************************************************************************
"""

from navhip.navhip import *
from navhip.navhipUtils import *
import json

"""
Signs a TX generated by Armory. That TX:

{
  'inputs': [{
    'p2shscript': '52210269694830114e4b1f6ef565ce4efb933681032d30333c80df713df6b60a4c62832102f43b905e9e35ccd22757faedf9eceb652dc9ba198a3904d43f4298def0213eb521037b9e3578dd3b5559d613bc2641931e6ce7d55a9d081b07347888d7d17a2b910253ae',
    'supporttxhash_be': '0c1676b8fc1adaca53221290e242b8eb80fd6b89aa83f2fa0106f87e13388300',
    'sequence': 4294967295,
    'keys': [{
      'dersighex': '',
      'pubkeyhex': '0269694830114e4b1f6ef565ce4efb933681032d30333c80df713df6b60a4c6283',
      'wltlochex': ''
    }, {
      'dersighex': '',
      'pubkeyhex': '02f43b905e9e35ccd22757faedf9eceb652dc9ba198a3904d43f4298def0213eb5',
      'wltlochex': ''
    }, {
      'dersighex': '',
      'pubkeyhex': '037b9e3578dd3b5559d613bc2641931e6ce7d55a9d081b07347888d7d17a2b9102',
      'wltlochex': ''
    }],
    'contriblabel': u '',
    'supporttxhash_le': '008338137ef80601faf283aa896bfd80ebb842e290122253cada1afcb876160c',
    'contribid': 'JLBercZk',
    'version': 1,
    'inputvalue': 46000000,
    'outpoint': '008338137ef80601faf283aa896bfd80ebb842e290122253cada1afcb876160c00000000',
    'magicbytes': '0b110907',
    'supporttx': '01000000013e9fe12917d854a0e093b982eaa46990289e2262f2db9fc1bd3f13718f3c806e010000006b483045022100af668e482e3ed363f51b36ddabad7cdf20d177104c92b8676a5b14f51107179602206c4ecd67544c74c6689ca453e2157d0c0b8a4608d85956429d2615275a51c66f01210374db359a004626daf2fcf10b8601f5f39438848a6733c768e88ce0ad398ae79dffffffff0280e7bd020000000017a914e2a227eb40dfce902f2c1d80ddafa798b16d22c3876c8fc846000000001976a914af58f09cf65b213bb9bd181a94e133b4ad4d6b2788ac00000000',
    'numkeys': 3,
    'supporttxhash': '0c1676b8fc1adaca53221290e242b8eb80fd6b89aa83f2fa0106f87e13388300',
    'supporttxoutindex': 0
  }],
  'fee': 10000,
  'locktimeint': 0,
  'outputs': [{
    'txoutvalue': 10000000,
    'authdata': '',
    'contriblabel': '',
    'p2shscript': '',
    'scripttypeint': 4,
    'isp2sh': True,
    'txoutscript': 'a914c0c3b6ada732c797881d00de6c350eec96e3d22287',
    'authmethod': 'NONE',
    'hasaddrstr': True,
    'contribid': '',
    'version': 1,
    'ismultisig': False,
    'magicbytes': '0b110907',
    'addrstr': '2NApUBXv4NB8pm834pHUajiUL6rvFaaj6N8',
    'scripttypestr': 'Standard (P2SH)',
    'wltlocator': ''
  }, {
    'txoutvalue': 35990000,
    'authdata': '',
    'contriblabel': '',
    'p2shscript': '',
    'scripttypeint': 4,
    'isp2sh': True,
    'txoutscript': 'a914e2a227eb40dfce902f2c1d80ddafa798b16d22c387',
    'authmethod': 'NONE',
    'hasaddrstr': True,
    'contribid': '',
    'version': 1,
    'ismultisig': False,
    'magicbytes': '0b110907',
    'addrstr': '2NDuYxRrmAs2fRcMj4ew2F41aFp2PN9yiV1',
    'scripttypestr': 'Standard (P2SH)',
    'wltlocator': ''
  }],
  'sumoutputs': 45990000,
  'suminputs': 46000000,
  'version': 1,
  'numoutputs': 2,
  'magicbytes': '0b110907',
  'locktimedate': '',
  'locktimeblock': 0,
  'id': '8jkccikU',
  'numinputs': 1
}

Input comes from vout[0] of 0c1676b8fc1adaca53221290e242b8eb80fd6b89aa83f2fa0106f87e13388300.
TX I want to generate is 0.10 to 2NApUBXv4NB8pm834pHUajiUL6rvFaaj6N8

The multisig address 2NDuYxRrmAs2fRcMj4ew2F41aFp2PN9yiV1 contains 0.46 BTC, and is generated
using the public keys 0'/0/0, 0'/0/1, and 0'/0/2 from the seed below.

"""

# Run on non configured dongle or dongle configured with test seed below

SEED = bytearray("1762F9A3007DBC825D0DD9958B04880284C88A10C57CF569BB3DADF7B1027F2D".decode('hex'))

# Armory supporttx
UTX = bytearray("01000000013e9fe12917d854a0e093b982eaa46990289e2262f2db9fc1bd3f13718f3c806e010000006b483045022100af668e482e3ed363f51b36ddabad7cdf20d177104c92b8676a5b14f51107179602206c4ecd67544c74c6689ca453e2157d0c0b8a4608d85956429d2615275a51c66f01210374db359a004626daf2fcf10b8601f5f39438848a6733c768e88ce0ad398ae79dffffffff0280e7bd020000000017a914e2a227eb40dfce902f2c1d80ddafa798b16d22c3876c8fc846000000001976a914af58f09cf65b213bb9bd181a94e133b4ad4d6b2788ac00000000".decode('hex'))
UTXO_INDEX = 0
OUTPUT = bytearray("02809698000000000017a914c0c3b6ada732c797881d00de6c350eec96e3d22287f02925020000000017a914e2a227eb40dfce902f2c1d80ddafa798b16d22c387".decode('hex'))
# Armory p2shscript
REDEEMSCRIPT = bytearray("52210269694830114e4b1f6ef565ce4efb933681032d30333c80df713df6b60a4c62832102f43b905e9e35ccd22757faedf9eceb652dc9ba198a3904d43f4298def0213eb521037b9e3578dd3b5559d613bc2641931e6ce7d55a9d081b07347888d7d17a2b910253ae".decode('hex'))

SIGNATURE_0 = bytearray("3044022056cb1b781fd04cfe6c04756ad56d02e5512f3fe7f411bc22d1594da5c815a393022074ad7f4d47af7c3f8a7ddf0ba2903f986a88649b0018ce1538c379b304a6a23801".decode('hex'))
SIGNATURE_1 = bytearray("304402205545419c4aded39c7f194b3f8c828f90e8d9352c756f7c131ed50e189c02f29a02201b160503d7310df49055b04a327e185fc22dfe68f433594ed7ce526d99a5026001".decode('hex'))
SIGNATURE_2 = bytearray("30440220634fbbfaaea74d42280a8c9e56c97418af04539f93458e85285d15462aec7712022041ba27a5644642a2f5b3c02610235ec2c6115bf4137bb51181cbc0a3a54dc0db01".decode('hex'))
TRANSACTION = bytearray("0100000001008338137ef80601faf283aa896bfd80ebb842e290122253cada1afcb876160c00000000fc004730440220634fbbfaaea74d42280a8c9e56c97418af04539f93458e85285d15462aec7712022041ba27a5644642a2f5b3c02610235ec2c6115bf4137bb51181cbc0a3a54dc0db0147304402205545419c4aded39c7f194b3f8c828f90e8d9352c756f7c131ed50e189c02f29a02201b160503d7310df49055b04a327e185fc22dfe68f433594ed7ce526d99a50260014c6952210269694830114e4b1f6ef565ce4efb933681032d30333c80df713df6b60a4c62832102f43b905e9e35ccd22757faedf9eceb652dc9ba198a3904d43f4298def0213eb521037b9e3578dd3b5559d613bc2641931e6ce7d55a9d081b07347888d7d17a2b910253aeffffffff02809698000000000017a914c0c3b6ada732c797881d00de6c350eec96e3d22287f02925020000000017a914e2a227eb40dfce902f2c1d80ddafa798b16d22c38700000000".decode('hex'))

SECONDFACTOR_1 = "RELAXED MODE Powercycle then confirm use of 0.46 BTC with PIN"

# Armory txoutscript
output = get_output_script([["0.1", bytearray("a914c0c3b6ada732c797881d00de6c350eec96e3d22287".decode('hex'))], ["0.3599", bytearray("a914e2a227eb40dfce902f2c1d80ddafa798b16d22c387".decode('hex'))]]);
if output<>OUTPUT:
	raise BTChipException("Invalid output script encoding");	

# Optional setup
dongle = getDongle(True)
app = navhip(dongle)
try:
  app.setup(navhip.OPERATION_MODE_RELAXED_WALLET, navhip.FEATURE_RFC6979, 111, 196, "1234", None, navhip.QWERTY_KEYMAP, SEED)
except Exception:
  pass
# Authenticate
app.verifyPin("1234")
# Get the trusted input associated to the UTXO
transaction = bitcoinTransaction(UTX)
print transaction
trustedInput = app.getTrustedInput(transaction, UTXO_INDEX)
# Start composing the transaction
app.startUntrustedTransaction(True, 0, [trustedInput], REDEEMSCRIPT)
app.finalizeInputFull(OUTPUT)
dongle.close()
# Wait for the second factor confirmation
# Done on the same application for test purposes, this is typically done in another window
# or another computer for bigger transactions
response = raw_input("Powercycle the dongle to get the second factor and powercycle again : ")
if not response.startswith(SECONDFACTOR_1):
  raise BTChipException("Invalid second factor")
# Get a reference to the dongle again, as it was disconnected
dongle = getDongle(True)
app = navhip(dongle)
# Replay the transaction, this time continue it since the second factor is ready
app.startUntrustedTransaction(False, 0, [trustedInput], REDEEMSCRIPT)
app.finalizeInputFull(OUTPUT)
# Provide the second factor to finalize the signature
signature1 = app.untrustedHashSign("0'/0/1", response[len(response) - 4:])
if signature1 <> SIGNATURE_1:
  raise BTChipException("Invalid signature1")

# Same thing for the second signature

app.verifyPin("1234")
app.startUntrustedTransaction(True, 0, [trustedInput], REDEEMSCRIPT)
app.finalizeInputFull(OUTPUT)
dongle.close()
response = raw_input("Powercycle the dongle to get the second factor and powercycle again : ")
if not response.startswith(SECONDFACTOR_1):
  raise BTChipException("Invalid second factor")
dongle = getDongle(True)
app = navhip(dongle)
app.startUntrustedTransaction(False, 0, [trustedInput], REDEEMSCRIPT)
app.finalizeInputFull(OUTPUT)
signature2 = app.untrustedHashSign("0'/0/2", response[len(response) - 4:])
if signature2 <> SIGNATURE_2:
  raise BTChipException("Invalid signature2")

# Finalize the transaction - build the redeem script and put everything together
inputScript = get_p2sh_input_script(REDEEMSCRIPT, [signature2, signature1])
transaction = format_transaction(OUTPUT, [ [ trustedInput['value'], inputScript] ])
print "Generated transaction : " + str(transaction).encode('hex')
if transaction <> TRANSACTION:
  raise BTChipException("Invalid transaction")
# The transaction is ready to be broadcast, enjoy

