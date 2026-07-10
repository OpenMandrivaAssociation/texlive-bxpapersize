%global tl_name bxpapersize
%global tl_revision 79217

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Synchronize output paper size with layout paper size
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bxpapersize
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpapersize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxpapersize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
As is well known, in LaTeX processing layout paper size specified by
document class options is not automatically applied to output paper
size. This package enables LaTeX authors to synchronize both kinds of
paper sizes.

