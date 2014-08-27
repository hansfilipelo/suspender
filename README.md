suspender
=========

Multi-threaded suspender for VMware ESXi virtual machines. Suspends all machines on a given host. Written in Python. 

LICENSE
=================================
    suspender - Multi-threaded suspender for VMware ESXi virtual machines
    Copyright (C) 2014  Hans-Filip Elo and Jens Edhammer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

REQUIREMENTS
=================================
Should run on any GNU environment that can run Python and SSH to a remote host. Tested on Debian, Ubuntu GNU/Linux and Mac OS X with ESXi 5.1 - but should work with ESXi version 2.5 up until the most recent version of ESXi. 

It's strongly recommended that key login is configured in order to use these scripts http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1002866

If you are running suspender with another (other than 5.1-5.5) ESXi-version, please confirm it's functioning status.

INSTRUCTIONS
=================================


Clone project, cd to folder: 

	git clone git://github.com/hansfilipelo/suspender.git
	cd suspender

Run:

	./suspender esxiHostname nrOfSimultaneousSuspends

To wake all machines: 

    ./wakeAllOnHost.sh esxiHostname

