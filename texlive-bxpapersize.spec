Name:		texlive-bxpapersize
Version:	63174
Release:	1
Summary:	Synchronize output paper size with layout paper size
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxpapersize
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpapersize.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpapersize.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
As is well known, in LaTeX processing layout paper size
specified by document class options is not automatically
applied to output paper size. This package enables LaTeX
authors to synchronize both kinds of paper sizes.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxpapersize
%doc %{_texmfdistdir}/doc/latex/bxpapersize

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
