import pytest
import requests
import jsonpath

# class TestDemo01:
#     @pytest.mark.parametrize()
#     def test_getrecord(self):
#         headers = {
#             "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhpQWFXS2Fmb1k2R3FZUFhJR3F0eGhKaktkbDVZZ3lUQ1U5UzFQLUVfQncifQ.eyJqdGkiOiJuY0FGZ1dwQ0wzTFltdzBFVGU0QzUiLCJzdWIiOiIxMTExMTU1NTA0ODA0Mjg4ODAwNSIsImlzcyI6Imh0dHBzOi8vYXV0aDAuYW1iZXJhaW5zaWRlci5jb20iLCJpYXQiOjE2MDY4MDk4NDUsImV4cCI6MTYwNjg5NjI0NSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSIsImF1ZCI6IkFwb2xsbyJ9.QMjhKYPTzsC_XkTzhxrUe97RO9MfiXY0zABxIT40jf0prArq3r5ycgdBxPyBhHnC-Wyz_p8sbp0QheMUlXEaEog9AEN7ORBGkmrvLHgsuYpY12HGBJPtAk9lVmwE753mJ8Vk6QTKNKDirbLLSYljoQvsm4nvCPPwnf_yBXtdCrV5mtfSVjTcbjYOCI2p8g1x8g5VA17q24a-shzuo2_mK9tr1UIRmpBmvEqQvVgGYSIpwUeGkkF2o3cVrm3AaL8w9syFESBmia6a2cLRdXNuIhn01QOj3k-YQvAUyF65m2oTrTUF3eDjDBrbRz91aj_mxzqR52pdLr3JOWZ8_m5fKw"}
#         res = requests.get('http://services.test.apollo.amberainsider.com/manage/client/ts/positions/sum',
#                            headers=headers)
#         r = res.json()
#         print(jsonpath.jsonpath(r, '$..errno'))
#         try:
#             assert jsonpath.jsonpath(r, '$..errno')[0] == 0
#         except:
#             print("error")