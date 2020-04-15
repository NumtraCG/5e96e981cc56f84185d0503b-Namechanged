import json
import Connectors
import Transformations
import AutoML
try:
    Namechanged_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e96e981cc56f84185d0503c", spark, "{'url': '', 'file_type': 'Delimeted', 'dbfs_token': '', 'dbfs_domain': '', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    Namechanged_AutoFE = Transformations.TransformationMain.run(["5e96e981cc56f84185d0503c"], {
                                                                "5e96e981cc56f84185d0503c": Namechanged_DBFS}, "5e96e981cc56f84185d0503d", spark, json.dumps({"FE": []}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionClassification(Namechanged_AutoFE, [], "")

except Exception as ex:
    print(ex)
