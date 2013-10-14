###
### RPM spec for the Netviz NETwork VIsualiZer
### ported by Sean Hinchee [henesy.dev@gmail.com]
###
Summary: A nice visualizer for ip's/mac addresses on the user's LAN
Name: Netviz
Provides: netviz
Version: 1.1
Release: 1
License: N/A
Group: Applications/Internet/
Source0: %{name}-%{version}.tar.bz2
URL: https://github.com/Poethemonk/NetViz
Vendor: Mark Miller 725mrm@gmail.com
Packager: Sean Hinchee henesy.dev@gmail.com
BuildArch: i686
BuildRoot:~/rpmbuild/netviz-root
Requires: python-pygame, python (<< 2.7), python (>= 2.5), python-central (>= 0.6.11), libc6 (>= 2.3.6-6~), libjpeg62 (>= 6b1), libpng12-0 (>= 1.2.13-4), libsdl-image1.2 (>= 1.2.10), libsdl-mixer1.2 (>= 1.2.6), libsdl-ttf2.0-0, libsdl1.2debian (>= 1.2.10-1), libsmpeg0, libx11-6, python-numpy, ttf-freefont
BuildRequires: 
%description
Netviz (short for NETwork VIsualiZer) is a Python program I cobbled together for a user to monitor devices on the user's LAN or a small section of the Internet. Essentially, it's a pretty interface for information on the MAC addresses and IPs of those devices. The range to search can be set either by the boundaries of the user's LAN using the "Find Range" button or through user-typed IPs. Also, there is a list of tracked MACs. If any of these tracked MACs appears on the LAN, the program shows the IP of this MAC

%prep

%build

%install
mv ~/rpmbuild/netviz-root /opt/

mv /opt/netviz-root /opt/netviz

ln -s /opt/netviz/netviz.py /usr/bin/netviz

%clean
rm -R ~/rpmbuild/netviz-root

%files
