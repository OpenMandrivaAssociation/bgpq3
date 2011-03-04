Summary:	bgp filtering automation for cisco and juniper routers
Name:		bgpq3
Version:	0.1.12
Release:	%mkrel 0
License:	GPL
Group:		Text tools
URL:		http://snar.spb.ru/prog/bgpq3/
Source:		http://snar.spb.ru/prog/bgpq3/%{name}-%{version}.tgz
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The bgpq3 ultility used to generate Cisco and Juniper prefix-lists, extended access-lists,
policy-statement terms and as-path lists based on RADB data.

%prep
%setup -q

%build
rm -fr %{buildroot}
%configure
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m 755 bgpq3 %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man8
install -D -m 644 bgpq3.8 %{buildroot}%{_mandir}/man8/

%clean
rm -fr %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man8/*
