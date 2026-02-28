%define		subver	2016-08-18
%define		ver		%(echo %{subver} | tr -d -)
%define		plugin	icalevents
%define		php_min_version 5.3.0
Summary:	Displays a calendar in iCalendar format according to a template
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/real-or-random/dokuwiki-plugin-icalevents/releases/download/%{subver}/dokuwiki-plugin-icalevents-%{subver}.zip
# Source0-md5:	518006eaaf16200112f2d5feb403a7f6
URL:		http://www.dokuwiki.org/plugin:icalevents
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	dokuwiki >= 20080505
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php(xml)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}
%define		find_lang 	%{_usrlibrpm}/dokuwiki-find-lang.sh %{buildroot}

%description
Many calendars can export their entries in the iCalendar (RFC 2445)
format. This plugin can read such an *.ics file from an URL, parse it
and display upcoming events as an HTML table.

%prep
%setup -qc
mv *icalevents*/* .

# empty file
rm index.html

%build
version=$(awk '/^date/{print $2}' plugin.info.txt)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.txt
%{plugindir}/conf
%{plugindir}/ics.png
%dir %{plugindir}/externals
%{plugindir}/externals/iCalcreator
