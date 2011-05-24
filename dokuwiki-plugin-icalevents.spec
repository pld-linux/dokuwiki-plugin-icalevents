%define		plugin	iCalEvents
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Parses an iCal calendar .ics file and renders it as an HTML table
Name:		dokuwiki-plugin-icalevents
Version:	20100501
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://public.doogie.de/projects/dokuwiki/plugin_iCalEvents_2.0.zip
# Source0-md5:	abef6798132ba03b74afd72ea62678ca
URL:		http://www.dokuwiki.org/plugin:icalevents
Patch0:		dformat.patch
Patch1:		reset-error.patch
Patch2:		allow-params.patch
Patch3:		relative-dates.patch
Patch4:		showCurrentWeek.patch
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Requires:	dokuwiki >= 20080505
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-date
Requires:	php-pcre
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
mv iCalEvents/* .
%undos -f php
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

version=$(awk -F"'" '/date/&&/=>/{print $4}' syntax.php)
if [ "$(echo "$version" | tr -d -)" != %{version} ]; then
	: %%{version} mismatch
#	exit 1
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
%{plugindir}/conf
