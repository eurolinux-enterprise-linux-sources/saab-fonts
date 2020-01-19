%global fontname saab
%global fontconf 67-%{fontname}.conf

Name:        %{fontname}-fonts
Version:     0.91
Release:     9%{?dist}
Summary:     Free Punjabi Unicode OpenType Font

Group:       User Interface/X

License:     GPLv2+ with exceptions
URL:         http://guca.sourceforge.net/typography/fonts/saab/
Source0:     http://downloads.sf.net/guca/saab.0.91.zip
Source1:     %{name}-fontconfig.conf
#Font file itself does not add exception text, so add it manually
#from http://guca.sourceforge.net/typography/fonts/saab/
Source2:     License_font_exception.txt
BuildArch:   noarch
BuildRequires: fontpackages-devel
Requires:    fontpackages-filesystem

%description 
This package provides a free OpenType Punjabi (Gurmukhi) font. 
Developed by Bhupinder Singh


%prep
%setup -q -c

%build
echo "Nothing to do in Build."

%install
install -m 0644 -p %{SOURCE2} .
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Saab.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%_font_pkg Saab.otf -f %{fontconf}
%doc License_font_exception.txt

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Parag <pnemade AT redhat DOT com> - 2.000-9
- Resolves:rh#880041 - Please include License exception text file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 08 2010 Parag <pnemade AT redhat.com> - 0.91-4
- Resolves: rh#562755: update license

* Tue Sep 04 2009 A S Alam <aalam@redhat.com> - 0.91-3
- Add fontconfig conf file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 2 2009 A S Alam <aalam@redhat.com> - 0.91-1
- New Package Build for Punjabi Unicode Font
