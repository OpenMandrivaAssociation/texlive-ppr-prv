# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/ppr-prv
# catalog-date 2007-01-13 23:45:25 +0100
# catalog-license lppl
# catalog-version 0.13c
Name:		texlive-ppr-prv
Version:	0.13c
Release:	8
Summary:	Prosper preview
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ppr-prv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ppr-prv.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class is used with LaTeX presentations using the prosper
class. ppr-prv stands for 'Prosper Preview'. The aim of this
class is to produce a printable version of the slides written
with Prosper, with two slides per page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ppr-prv/HAP-ppr-prv.def
%{_texmfdistdir}/tex/latex/ppr-prv/ppr-prv.cls
%doc %{_texmfdistdir}/doc/latex/ppr-prv/README
%doc %{_texmfdistdir}/doc/latex/ppr-prv/ppr-prv.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ppr-prv/ppr-prv.dtx
%doc %{_texmfdistdir}/source/latex/ppr-prv/ppr-prv.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.13c-2
+ Revision: 755045
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.13c-1
+ Revision: 719292
- texlive-ppr-prv
- texlive-ppr-prv
- texlive-ppr-prv
- texlive-ppr-prv

