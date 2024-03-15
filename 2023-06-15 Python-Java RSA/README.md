[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11244868&assignment_repo_type=AssignmentRepo)
# Minecraft Scure API
This is the README file for Assignment 3 in Programming Studio 2 (COSC2804).

## Video
[YouTube Video](https://youtu.be/JiRLT1NP8i8)

# Files breakdown
Below is a list of all notable files and folders in this repository, and their purpose.
| File/folder                  | Description                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------|
| ./ELCI-master                | Altered ELCI Java plugin source code                                                                        |
| ./mcpielcimaster             | Altered MCPI ELCI Python source code                                                                        |
| ./mcpielcimasterunsecure     | **Original, unsecure** MCPI ELCI Python source code                                                         |
| ./server                     | Minecraft Java server files                                                                                 |
| ./mcpi_sec                   | Contains everything needed to run demo, **it is recommended to follow the instructions below instead**      |
| elci-1.12.1.jar              | Original unsecure ELCI Java Bukkit plugin                                                                   |
| mcpi_sec.py                  | Testing script that imports our altered MCPI Python code                                                    |
| mcpi_unsec.py                | Testing script that imports the unsecure MCPI Python code                                                   |
| package_and_run_server.sh    | A simple Shell script to package ELCI Java plugin, move it to ./server/plugins, and start the server        |
| run_unsecure_server.sh       | A simple Shell script to move the unsecure Java plugin from root to ./server/plugins, and start the server. |
| run_secure_server.sh       | A simple Shell script to move the secure Java plugin from ./mcpi_sec to ./server/plugins, and start the server. **Recommended if maven is not installed**. |
| requirements.txt             | A list of all python requirements needed                                                                    |
| ./mcpi_sec/asmnt3_report.pdf | A pdf file containing our written report                                                                    |


*Only ``RemoteSession.java`` was altered in ./ELCI-master/src/main/java/net/rozukke/elci, and only ``connection.py`` was altered in ./mcpielcimaster/mcpi*

# How to run the program
Most versions of python 3.10 - 3.11 should work fine. We developed on 3.10.6.

1. Download this entire github repo.

2. Open a terminal window and navigate to the root of this repository

3. Once the CWD is the root of this repository, install the python requirements:
    ```
    pip install -r requirements.txt
    ```
From here, you can choose any of the three Shell scripts to run the server
- For a secure server, run the command:
    ```
    bash run_secure_server.sh
    ```
    Followed by: ``python mcpi_sec.py``

- For an unsecure server, run the command:
    ```
    bash run_unsecure_server.sh
    ```
    Followed by: ``python mcpi_unsec.py``
    
- To run the server with a newly-packaged .jar from Maven, run the command:
    ```
    bash package_and_run_server.sh
    ```
    Followed by: ``python mcpi_sec.py``

# Mandatory: Student contributions
Vidhathra - 25%
- CCA secure techniques
- Report section, how encrypt then mac
- Video voiceover

Cathy - 25%
- CCA secure techniques
- Report section, security/tradeoffs
- Video voiceover

William - 25%
- CCA secure techniques
- Code implementation
- Video voiceover

Andrew - 25%
- CCA secure techniques
- Code implementation
- Video voiceover