from langchain_community.tools import ShellTool

cli = ShellTool()
result = cli.invoke('whoami')
print(result) 