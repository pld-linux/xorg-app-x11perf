Summary:	x11perf application - X11 server performance test program
Summary(pl.UTF-8):	Aplikacja x11perf do testowania wydajności serwera X11
Name:		xorg-app-x11perf
Version:	1.5.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/x11perf-%{version}.tar.bz2
# Source0-md5:	66e4aa4645f83809071eb69553ed0222
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%description -l pl.UTF-8
Program x11perf uruchamia jeden lub więcej testów wydajnościowych i
informuje jak szybko serwer X jest w stanie wykonać te testy.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%dir %{_libdir}/X11/x11perfcomp
%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*
%{_mandir}/man1/Xmark.1x*
%{_mandir}/man1/x11perf.1x*
%{_mandir}/man1/x11perfcomp.1x*
