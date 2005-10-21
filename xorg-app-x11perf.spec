Summary:	x11perf application
Summary(pl):	Aplikacja x11perf
Name:		xorg-app-x11perf
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/x11perf-%{version}.tar.bz2
# Source0-md5:	6521aa2ec6909c81609e7c16593dfb1a
#Patch0:		x11perf-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
x11perf application.

%description -l pl
Aplikacja x11perf.

%prep
%setup -q -n x11perf-%{version}
#%patch0 -p1

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
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*
%{_mandir}/man1x/*.1x*
