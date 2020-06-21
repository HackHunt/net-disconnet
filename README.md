## Net Disconnect

- Drops the flow of packets, thus makes the target's internet connection not responding.

### Supports Platform: Linux, Debain

### How to use:
- Convert the setup.sh into executable
	> **chmod 755 setup.sh**
- Run setup.sh
	> **./setup.sh**
- Run the Python Script with root privileges.
    > **sudo python net_disconnet.py** 

### Available Arguments:
- **-h or --help:** *Displays all the available options.*
- **-q or --queue-num:** *Optional. Is used to define queue number for IP tables.*

- **Note:** 
	- You need to be connected to the same network.
	- You need to be the MITM. For this check our [Website](https://hack-hunt.blogspot.com/) and GitHub.

### Programming Language: Python 2.7

### Libraries Used:
- **subprocess:** The *subprocess* module allows you to spawn new processes, connect to their
input/output/error pipes, and obtain their return codes. Used to interact with command line
arguments.
- **argparse:** The *argparse* module makes it easy to write user-friendly command-line interfaces. The
program defines what arguments it requires, and argparse will figure out how to parse those out of
sys.argv.
- **sys:** The *sys* module provides access to some variables used or maintained by the interpreter and
to functions that interact strongly with the interpreter.
- **os:** The *os* module provides a portable way of using operating system dependent functionality.
- **netfilterqueue:** The *netfilerqueue* module is used to intercept packet flows.
- **random:** The *random* module implements pseudo-random number generators for various
distributions. Used to generaye quene number of IP tables.

### Licensed: GNU General Public License, version 3

### Developer Information:
- **Website:** [Hack Hunt](https://hack-hunt.blogspot.com/)
- **Contact:** hh.hackunt@gmail.com
- **Youtube:** [Hack Hunt](https://youtube.com/hackhunt) 
- **Instagram:** [hh.hackhunt](https://www.instagram.com/hh.hackhunt/)
- **Facebook:** [hh.hackhunt](https://www.facebook.com/hh.hackhunt/)
- **Twitter:** [hh_hackhunt](https://twitter.com/hh_hackhunt/)
