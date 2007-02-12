Summary:	x11perf application
Summary(pl.UTF-8):   Aplikacja x11perf
Name:		xorg-app-x11perf
Version:	1.4.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/x11perf-%{version}.tar.bz2
# Source0-md5:	fd06c8b8e3572a0e14af65a49e0dd7d1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x11perf application.

%description -l pl.UTF-8
Aplikacja x11perf.

%prep
%setup -q -n x11perf-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%dir %{_libdir}/X11/x11perfcomp
%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*
%{_mandir}/man1/Xmark.1x*
%{_mandir}/man1/x11perf.1x*
%{_mandir}/man1/x11perfcomp.1x*
