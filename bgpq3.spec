Summary:	BGP filtering automation for cisco and juniper routers


Name:		bgpq3
Version:	0.1.31
Release:	1
License:	GPLv2
Group:		Text tools
URL:		https://snar.spb.ru/prog/bgpq3/
Source:		http://snar.spb.ru/prog/bgpq3/%{name}-%{version}.tgz


%description
The bgpq3 ultility used to generate Cisco and 
Juniper prefix-lists, extended access-lists,
policy-statement terms and as-path lists 
based on RADB data.

%prep
%setup -q

%build
%configure
%make

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m 755 bgpq3 %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man8
install -D -m 644 bgpq3.8 %{buildroot}%{_mandir}/man8/

%files
%{_bindir}/*
%{_mandir}/man8/*




