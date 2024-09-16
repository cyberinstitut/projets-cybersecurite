import "hash"


rule metasploit_office_word_macro_vbaproject_bin_zipped {
    meta:
        author = "DidierStevens"
        date = "2017/08/20"
        description = "Source code put in public domain by Didier Stevens, no Copyright https://DidierStevens.com, Use at your own risk! Detect .docm files created with Metasploit's office_word_macro exploit"

    strings:
        $a = {776F72642F76626150726F6A6563742E62696EED3B0D7853D775E75D3D0959B6B1640C7120908B4CB04C2421C9B22D3B98EADF86D860B0032421C1FA79C222B2A44A4FD8E4A795B1D3928435AC5D33CAD20E42DAA62DEB489AB07EE9BA8976FB42F3B5DF48D3ED4BBA7531C99666FDBE0E4AB32F69B6C43BF7BD275BFE2350BA}
    condition:
        $a and hash.md5(@a + 19, 5962) == "e5995aba8551f30cc15c87ee49fb834a"
}


rule Contains_VBA_macro_code
{
	meta:
		author = "evild3ad"
		description = "Detect a MS Office document with embedded VBA macro code"
		date = "2016-01-09"
		filetype = "Office documents"

	strings:
		$officemagic = { D0 CF 11 E0 A1 B1 1A E1 }
		$zipmagic = "PK"
		$97str1 = "_VBA_PROJECT_CUR" wide
		$97str2 = "VBAProject"
		$97str3 = { 41 74 74 72 69 62 75 74 00 65 20 56 42 5F } // Attribute VB_
		$xmlstr1 = "vbaProject.bin"
		$xmlstr2 = "vbaData.xml"
	condition:
		($officemagic at 0 and any of ($97str*)) or ($zipmagic at 0 and any of ($xmlstr*))
}
