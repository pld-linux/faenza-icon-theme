Summary:	Icon theme designed for Equinox GTK theme
Name:		faenza-icon-theme
Version:	1.1
Release:	1
License:	GPL v3
Group:		X11/Applications
URL:		http://tiheum.deviantart.com/art/Faenza-Icons-173323228
Source0:	https://faenza-icon-theme.googlecode.com/files/%{name}_%{version}.tar.gz
# Source0-md5:	a7385a92226a3b3ab3949952149fe3a3
Requires(post,postun):	gtk-update-icon-cache
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contains icons for Equinox GTK theme

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/icons

cp -a Faenza* $RPM_BUILD_ROOT%{_datadir}/icons

for f in Faenza*; do
	touch $RPM_BUILD_ROOT%{_iconsdir}/$f/icon-theme.cache
done

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Faenza
%update_icon_cache Faenza-Dark
%update_icon_cache Faenza-Darker
%update_icon_cache Faenza-Darkest

%postun
%update_icon_cache Faenza
%update_icon_cache Faenza-Dark
%update_icon_cache Faenza-Darker
%update_icon_cache Faenza-Darkest

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%dir %{_iconsdir}/Faenza*
%{_iconsdir}/Faenza*/[a-hj-su-z]*
%{_iconsdir}/Faenza*/index.theme
%ghost %{_iconsdir}/Faenza*/icon-theme.cache
