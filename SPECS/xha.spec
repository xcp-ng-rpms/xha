Summary: xha - XenServer proprietary HA daemon
Name:    xha
Version: 10.1.0
Release: 1%{?dist}
License: GPLv2
URL:     https://github.com/xenserver/xha

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xha/archive?at=v10.1.0&prefix=xha-10.1.0&format=tar.gz#/xha-10.1.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/xha/archive?at=v10.1.0&prefix=xha-10.1.0&format=tar.gz#/xha-10.1.0.tar.gz) = 20b7e5244f9e25b199ea8e3ef5b935f4e9b4247d


BuildRequires: libxml2-devel
BuildRequires: xen-devel

Requires: portreserve

%description
This package contains the HA heartbeating daemon used for XenServer's HA feature

%prep
%autosetup -p1

%build
%{?cov_wrap} make

%install
DESTDIR=$RPM_BUILD_ROOT make install

%files
%{_sysconfdir}/logrotate.d/xha
%{_sysconfdir}/portreserve/xhad
%{_libexecdir}/xapi/cluster-stack/xhad/calldaemon
%{_libexecdir}/xapi/cluster-stack/xhad/cleanupwatchdog
%{_libexecdir}/xapi/cluster-stack/xhad/dumpstatefile
%{_libexecdir}/xapi/cluster-stack/xhad/ha_clear_excluded
%{_libexecdir}/xapi/cluster-stack/xhad/ha_disarm_fencing
%{_libexecdir}/xapi/cluster-stack/xhad/ha_errnorc
%{_libexecdir}/xapi/cluster-stack/xhad/ha_null
%{_libexecdir}/xapi/cluster-stack/xhad/ha_propose_master
%{_libexecdir}/xapi/cluster-stack/xhad/ha_query_liveset
%{_libexecdir}/xapi/cluster-stack/xhad/ha_rc
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_excluded
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_host_weight
%{_libexecdir}/xapi/cluster-stack/xhad/ha_set_pool_state
%{_libexecdir}/xapi/cluster-stack/xhad/ha_start_daemon
%{_libexecdir}/xapi/cluster-stack/xhad/ha_stop_daemon
%{_libexecdir}/xapi/cluster-stack/xhad/weightctl
%{_libexecdir}/xapi/cluster-stack/xhad/writestatefile
%{_libexecdir}/xapi/cluster-stack/xhad/xhad

%changelog
* Mon Jul 01 2019 Christian Lindig <christian.lindig@citrix.com> - 10.1.0-1
- XSI-301: Print errno when watchdog hypercall fails.
- XSI-301: remove duplicated unlock_pages lines
- CA-315962 cleanupwatchdog: Use hypercall's errno
- CA-315962 cleanupwatchdog: exit when encountering errors on hypercalls
- CA-315962 cleanupwatchdog: restrict hypercalls to disable watchdogs
- CA-315962 cleanupwatchdog: simplify hypercall call handling
- CA-315962 cleanupwatchdog: Allow resetting watchdog slots without an HA file
- CA-315962: Flush watchdog slots on HA startup

* Tue Nov 8 2016 Euan Harris <euan.harris@citrix.com> - 10.0.1-1
- Include Git commit metadata in source archive

* Tue Oct 18 2016 Euan Harris <euan.harris@citrix.com> - 10.0.0-1
- Build from GitHub sources

* Mon Oct 17 2016 Vivek Kumar Chaubey <vivekkumar.chaubey@citrix.com> - 7.0.91-248
- Build using transformer
