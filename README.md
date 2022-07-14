# PythonStreamDeck

This is a Python script that will control OBS using <a href="https://github.com/obsproject/obs-websocket">obs-websocket</a> and <a href="https://github.com/IRLToolkit/simpleobsws">simpleobsws</a>.

# Install Instructions

<ol>
    <li>Download Python</li>
    <li>Download this repository</li>
    <li>Install simpleobsws by going into the directory "simpleobsws" and running "python setup.py install" (Windows) or "python3 setup.py install" (Linux. You may have to use sudo permissions to install.)</li>
    <li>Go back to the default directory, "PythonStreamDeck" and run "pip install -r requirements.txt" if that doesn't work, do "pip3 install -r requirements.txt"</li>
    <li>Download and install obs-websocket from the link above</li>
    <li>Configure obs-websocket (the settings window should show up the next time you launch OBS. Remember these settings</li>
    <li>Edit the "obsRequests.py" with your preferred text editor and find the line which starts with "ws = simpleobsws.obsws." This is where you will but the settings from that obs-websocket window. If you are running this program and OBS on the same computer, then you can leave the host as it is. Otherwise, you will need to input the IP address of the machine running OBS. Fill in the "port" and "password." The password can be blank, just leave it as it is.</li>
    <li>Now that everything is setup, Windows users should run the "run.bat" file. You may need to allow Python througt your firewall. Linux users should run the "run.sh" file. Linux users may need to provide permissions to the script to run.</li>
</ol>

# To Do

:heavy_check_mark: Read yaml file

:heavy_check_mark: Control OBS

:heavy_check_mark: Create dynamic HTML file

:heavy_check_mark: split code into separate Python files for more organization

:x: Add GUI in the HTML that will allow user to add new buttons to the page

:x: make better instructions

:x: make video explaining how to install

:x: use the dynamic updates
