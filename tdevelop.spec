%bcond clang 1
%bcond gamin 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tdevelop
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Summary:	Integrated Development Environment for C++/C
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		Development/Tools
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:	%{name}-rpmlintrc

Requires:	%{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_BUILDTOOL_ALL=ON -DWITH_LANGUAGE_ALL=ON
BuildOption:    -DWITH_VCS_ALL=OFF -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	tqt3-apps-devel >= 3.5.0
BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	trinity-tdesdk-devel >= %{tde_version}

Obsoletes:	trinity-kdevelop < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdevelop = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes
BuildRequires:	desktop-file-utils
BuildRequires:  make

Requires:	perl
Requires:	tqt3-designer >= 3.5.0
Requires:	libtqt3-mt-devel >= 3.5.0
Requires:	gettext
Requires:	ctags


# LIBIDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# PCRE2 support
BuildRequires:  pkgconfig(libpcre2-posix)

# DB5 support
BuildRequires:  db-devel

# FLEX support
BuildRequires:	flex
Requires: flex >= 2.5.4

# SVN support
BuildRequires:	pkgconfig(libsvn_client)

# NEON support
BuildRequires:	pkgconfig(neon)

# OPENLDAP support
BuildRequires:  pkgconfig(ldap)

# LIBACL support
BuildRequires:  pkgconfig(libacl)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

# PYTHON support
%global python python3
%global __python %__python3


%description
The TDevelop Integrated Development Environment provides many features
that developers need as well as providing a unified interface to programs
like gdb, the C/C++ compiler, and make. TDevelop manages or provides:

All development tools needed for C++ programming like Compiler,
Linker, automake and autoconf; KAppWizard, which generates complete,
ready-to-go sample applications; Classgenerator, for creating new
classes and integrating them into the current project; File management
for sources, headers, documentation etc. to be included in the
project; The creation of User-Handbooks written with SGML and the
automatic generation of HTML-output with the KDE look and feel;
Automatic HTML-based API-documentation for your project's classes with
cross-references to the used libraries; Internationalization support
for your application, allowing translators to easily add their target
language to a project;

tdevelop also includes WYSIWYG (What you see is what you get)-creation
of user interfaces with a built-in dialog editor; Debugging your
application by integrating KDbg; Editing of project-specific pixmaps
with KIconEdit; The inclusion of any other program you need for
development by adding it to the "Tools"-menu according to your
individual needs.

%files
%defattr(-,root,root,-)
%{tde_prefix}/bin/kdevassistant
%{tde_prefix}/bin/kdevdesigner
%{tde_prefix}/bin/tdevelop
%{tde_prefix}/bin/tdevelop-htdig
%{tde_prefix}/bin/kdevprj2kdevelop
%{tde_prefix}/bin/kdevprofileeditor
%{tde_prefix}/%{_lib}/tdeconf_update_bin/kdev-gen-settings-tdeconf_update
%config(noreplace) %{_sysconfdir}/trinity/kdevassistantrc
%config(noreplace) %{_sysconfdir}/trinity/tdeveloprc
%{tde_prefix}/share/applications/tde/kdevassistant.desktop
%{tde_prefix}/share/applications/tde/kdevdesigner.desktop
%{tde_prefix}/share/applications/tde/tdevelop.desktop
%{tde_prefix}/share/applications/tde/tdevelop_c_cpp.desktop
%{tde_prefix}/share/applications/tde/tdevelop_kde_cpp.desktop
%{tde_prefix}/share/applications/tde/tdevelop_ruby.desktop
%{tde_prefix}/share/applications/tde/tdevelop_scripting.desktop
%{tde_prefix}/%{_lib}/trinity/tdeio_chm.la
%{tde_prefix}/%{_lib}/trinity/tdeio_chm.so
%{tde_prefix}/%{_lib}/trinity/tdeio_csharpdoc.la
%{tde_prefix}/%{_lib}/trinity/tdeio_csharpdoc.so
%{tde_prefix}/%{_lib}/trinity/tdeio_perldoc.la
%{tde_prefix}/%{_lib}/trinity/tdeio_perldoc.so
%{tde_prefix}/%{_lib}/trinity/tdeio_pydoc.la
%{tde_prefix}/%{_lib}/trinity/tdeio_pydoc.so
%{tde_prefix}/%{_lib}/trinity/libdocchmplugin.la
%{tde_prefix}/%{_lib}/trinity/libdocchmplugin.so
%{tde_prefix}/%{_lib}/trinity/libdoccustomplugin.la
%{tde_prefix}/%{_lib}/trinity/libdoccustomplugin.so
%{tde_prefix}/%{_lib}/trinity/libdocdevhelpplugin.la
%{tde_prefix}/%{_lib}/trinity/libdocdevhelpplugin.so
%{tde_prefix}/%{_lib}/trinity/libdocdoxygenplugin.la
%{tde_prefix}/%{_lib}/trinity/libdocdoxygenplugin.so
%{tde_prefix}/%{_lib}/trinity/libdockdevtocplugin.la
%{tde_prefix}/%{_lib}/trinity/libdockdevtocplugin.so
%{tde_prefix}/%{_lib}/trinity/libdocqtplugin.la
%{tde_prefix}/%{_lib}/trinity/libdocqtplugin.so
%{tde_prefix}/%{_lib}/trinity/libkchmpart.la
%{tde_prefix}/%{_lib}/trinity/libkchmpart.so
%{tde_prefix}/%{_lib}/trinity/libkdevabbrev.la
%{tde_prefix}/%{_lib}/trinity/libkdevabbrev.so
%{tde_prefix}/%{_lib}/trinity/libkdevadaproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevadaproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevadasupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevadasupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevantproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevantproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevappview.la
%{tde_prefix}/%{_lib}/trinity/libkdevappview.so
%{tde_prefix}/%{_lib}/trinity/libkdevappwizard.la
%{tde_prefix}/%{_lib}/trinity/libkdevappwizard.so
%{tde_prefix}/%{_lib}/trinity/libkdevastyle.la
%{tde_prefix}/%{_lib}/trinity/libkdevastyle.so
%{tde_prefix}/%{_lib}/trinity/libkdevautoproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevautoproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevbashsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevbashsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevbookmarks.la
%{tde_prefix}/%{_lib}/trinity/libkdevbookmarks.so
%{tde_prefix}/%{_lib}/trinity/libkdevclassview.la
%{tde_prefix}/%{_lib}/trinity/libkdevclassview.so
%{tde_prefix}/%{_lib}/trinity/libkdevcppsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevcppsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevcsharpsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevcsharpsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevctags2.la
%{tde_prefix}/%{_lib}/trinity/libkdevctags2.so
%{tde_prefix}/%{_lib}/trinity/libkdevcustompcsimporter.la
%{tde_prefix}/%{_lib}/trinity/libkdevcustompcsimporter.so
%{tde_prefix}/%{_lib}/trinity/libkdevcustomproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevcustomproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevdccoptions.la
%{tde_prefix}/%{_lib}/trinity/libkdevdccoptions.so
%{tde_prefix}/%{_lib}/trinity/libkdevdebugger.la
%{tde_prefix}/%{_lib}/trinity/libkdevdebugger.so
%{tde_prefix}/%{_lib}/trinity/libkdevdesignerpart.la
%{tde_prefix}/%{_lib}/trinity/libkdevdesignerpart.so
%{tde_prefix}/%{_lib}/trinity/libkdevdiff.la
%{tde_prefix}/%{_lib}/trinity/libkdevdiff.so
%{tde_prefix}/%{_lib}/trinity/libkdevdistpart.la
%{tde_prefix}/%{_lib}/trinity/libkdevdistpart.so
%{tde_prefix}/%{_lib}/trinity/libkdevdocumentation.la
%{tde_prefix}/%{_lib}/trinity/libkdevdocumentation.so
%{tde_prefix}/%{_lib}/trinity/libkdevdoxygen.la
%{tde_prefix}/%{_lib}/trinity/libkdevdoxygen.so
%{tde_prefix}/%{_lib}/trinity/libkdeveditorchooser.la
%{tde_prefix}/%{_lib}/trinity/libkdeveditorchooser.so
%{tde_prefix}/%{_lib}/trinity/libkdevfilecreate.la
%{tde_prefix}/%{_lib}/trinity/libkdevfilecreate.so
%{tde_prefix}/%{_lib}/trinity/libkdevfilegroups.la
%{tde_prefix}/%{_lib}/trinity/libkdevfilegroups.so
%{tde_prefix}/%{_lib}/trinity/libkdevfilelist.la
%{tde_prefix}/%{_lib}/trinity/libkdevfilelist.so
%{tde_prefix}/%{_lib}/trinity/libkdevfileselector.la
%{tde_prefix}/%{_lib}/trinity/libkdevfileselector.so
%{tde_prefix}/%{_lib}/trinity/libkdevfileview.la
%{tde_prefix}/%{_lib}/trinity/libkdevfileview.so
%{tde_prefix}/%{_lib}/trinity/libkdevfilter.la
%{tde_prefix}/%{_lib}/trinity/libkdevfilter.so
%{tde_prefix}/%{_lib}/trinity/libkdevfortransupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevfortransupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevfpcoptions.la
%{tde_prefix}/%{_lib}/trinity/libkdevfpcoptions.so
%{tde_prefix}/%{_lib}/trinity/libkdevfullscreen.la
%{tde_prefix}/%{_lib}/trinity/libkdevfullscreen.so
%{tde_prefix}/%{_lib}/trinity/libkdevgccoptions.la
%{tde_prefix}/%{_lib}/trinity/libkdevgccoptions.so
%{tde_prefix}/%{_lib}/trinity/libkdevgrepview.la
%{tde_prefix}/%{_lib}/trinity/libkdevgrepview.so
%{tde_prefix}/%{_lib}/trinity/libkdevjavasupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevjavasupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevtdelibsimporter.la
%{tde_prefix}/%{_lib}/trinity/libkdevtdelibsimporter.so
%{tde_prefix}/%{_lib}/trinity/libkdevkonsoleview.la
%{tde_prefix}/%{_lib}/trinity/libkdevkonsoleview.so
%{tde_prefix}/%{_lib}/trinity/libkdevmakeview.la
%{tde_prefix}/%{_lib}/trinity/libkdevmakeview.so
%{tde_prefix}/%{_lib}/trinity/libkdevopenwith.la
%{tde_prefix}/%{_lib}/trinity/libkdevopenwith.so
%{tde_prefix}/%{_lib}/trinity/libkdevpartexplorer.la
%{tde_prefix}/%{_lib}/trinity/libkdevpartexplorer.so
%{tde_prefix}/%{_lib}/trinity/libkdevpascalproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevpascalproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevpascalsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevpascalsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevperlsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevperlsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevpgioptions.la
%{tde_prefix}/%{_lib}/trinity/libkdevpgioptions.so
%{tde_prefix}/%{_lib}/trinity/libkdevphpsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevphpsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevpythonsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevpythonsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevqtimporter.la
%{tde_prefix}/%{_lib}/trinity/libkdevqtimporter.so
%{tde_prefix}/%{_lib}/trinity/libkdevquickopen.la
%{tde_prefix}/%{_lib}/trinity/libkdevquickopen.so
%{tde_prefix}/%{_lib}/trinity/libkdevrbdebugger.la
%{tde_prefix}/%{_lib}/trinity/libkdevrbdebugger.so
%{tde_prefix}/%{_lib}/trinity/libkdevregexptest.la
%{tde_prefix}/%{_lib}/trinity/libkdevregexptest.so
%{tde_prefix}/%{_lib}/trinity/libkdevreplace.la
%{tde_prefix}/%{_lib}/trinity/libkdevreplace.so
%{tde_prefix}/%{_lib}/trinity/libkdevrubysupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevrubysupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevscripting.la
%{tde_prefix}/%{_lib}/trinity/libkdevscripting.so
%{tde_prefix}/%{_lib}/trinity/libkdevscriptproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevscriptproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevsnippet.la
%{tde_prefix}/%{_lib}/trinity/libkdevsnippet.so
%{tde_prefix}/%{_lib}/trinity/libkdevsqlsupport.la
%{tde_prefix}/%{_lib}/trinity/libkdevsqlsupport.so
%{tde_prefix}/%{_lib}/trinity/libkdevtexttools.la
%{tde_prefix}/%{_lib}/trinity/libkdevtexttools.so
%{tde_prefix}/%{_lib}/trinity/libkdevtipofday.la
%{tde_prefix}/%{_lib}/trinity/libkdevtipofday.so
%{tde_prefix}/%{_lib}/trinity/libkdevtools.la
%{tde_prefix}/%{_lib}/trinity/libkdevtools.so
%{tde_prefix}/%{_lib}/trinity/libkdevtrollproject.la
%{tde_prefix}/%{_lib}/trinity/libkdevtrollproject.so
%{tde_prefix}/%{_lib}/trinity/libkdevuichooser.la
%{tde_prefix}/%{_lib}/trinity/libkdevuichooser.so
%{tde_prefix}/%{_lib}/trinity/libkdevvalgrind.la
%{tde_prefix}/%{_lib}/trinity/libkdevvalgrind.so
%{tde_prefix}/%{_lib}/trinity/libkdevvcsmanager.la
%{tde_prefix}/%{_lib}/trinity/libkdevvcsmanager.so
%{tde_prefix}/share/apps/tdeconf_update/
%{tde_prefix}/share/apps/kdevabbrev/
%{tde_prefix}/share/apps/kdevadaproject/
%{tde_prefix}/share/apps/kdevadasupport/
%{tde_prefix}/share/apps/kdevantproject/
%{tde_prefix}/share/apps/kdevappoutputview/
%{tde_prefix}/share/apps/kdevappwizard/
%{tde_prefix}/share/apps/kdevassistant/
%{tde_prefix}/share/apps/kdevastyle/
%{tde_prefix}/share/apps/kdevautoproject/
%{tde_prefix}/share/apps/kdevbashsupport/
%{tde_prefix}/share/apps/kdevclassview/
%{tde_prefix}/share/apps/kdevcppsupport/
%{tde_prefix}/share/icons/hicolor/*/actions/breakpoint_add.png
%{tde_prefix}/share/icons/hicolor/*/actions/breakpoint_delete.png
%{tde_prefix}/share/icons/hicolor/*/actions/breakpoint_delete_all.png
%{tde_prefix}/share/icons/hicolor/*/actions/breakpoint_edit.png
%{tde_prefix}/share/icons/hicolor/*/actions/ktip.png
%{tde_prefix}/share/icons/hicolor/*/apps/kdevassistant.png
%{tde_prefix}/share/icons/hicolor/*/apps/kdevdesigner.png
%{tde_prefix}/share/icons/hicolor/*/apps/tdevelop.png
%{tde_prefix}/share/icons/locolor/*/actions/tdevelop_tip.png
%{tde_prefix}/share/mimelnk/application/x-tdevelop.desktop
%{tde_prefix}/share/services/chm.protocol
%{tde_prefix}/share/services/csharpdoc.protocol
%{tde_prefix}/share/services/docchmplugin.desktop
%{tde_prefix}/share/services/doccustomplugin.desktop
%{tde_prefix}/share/services/docdevhelpplugin.desktop
%{tde_prefix}/share/services/docdoxygenplugin.desktop
%{tde_prefix}/share/services/dockdevtocplugin.desktop
%{tde_prefix}/share/services/docqtplugin.desktop
%{tde_prefix}/share/services/kchmpart.desktop
%{tde_prefix}/share/services/kdevabbrev.desktop
%{tde_prefix}/share/services/kdevadaproject.desktop
%{tde_prefix}/share/services/kdevadasupport.desktop
%{tde_prefix}/share/services/kdevantproject.desktop
%{tde_prefix}/share/services/kdevappoutputview.desktop
%{tde_prefix}/share/services/kdevappwizard.desktop
%{tde_prefix}/share/services/kdevastyle.desktop
%{tde_prefix}/share/services/kdevautoproject.desktop
%{tde_prefix}/share/services/kdevbashsupport.desktop
%{tde_prefix}/share/services/kdevbookmarks.desktop
%{tde_prefix}/share/services/kdevclassview.desktop
%{tde_prefix}/share/services/kdevcppsupport.desktop
%{tde_prefix}/share/services/kdevcsharpsupport.desktop
%{tde_prefix}/share/services/kdevcsupport.desktop
%{tde_prefix}/share/services/kdevctags2.desktop
%{tde_prefix}/share/services/kdevcustomproject.desktop
%{tde_prefix}/share/services/kdevdccoptions.desktop
%{tde_prefix}/share/services/kdevdebugger.desktop
%{tde_prefix}/share/services/kdevdesigner_part.desktop
%{tde_prefix}/share/services/kdevdiff.desktop
%{tde_prefix}/share/services/kdevdistpart.desktop
%{tde_prefix}/share/services/kdevdocumentation.desktop
%{tde_prefix}/share/services/kdevdoxygen.desktop
%{tde_prefix}/share/services/kdeveditorchooser.desktop
%{tde_prefix}/share/services/kdevfilecreate.desktop
%{tde_prefix}/share/services/kdevfilegroups.desktop
%{tde_prefix}/share/services/kdevfilelist.desktop
%{tde_prefix}/share/services/kdevfileselector.desktop
%{tde_prefix}/share/services/kdevfileview.desktop
%{tde_prefix}/share/services/kdevfilter.desktop
%{tde_prefix}/share/services/kdevfortransupport.desktop
%{tde_prefix}/share/services/kdevfpcoptions.desktop
%{tde_prefix}/share/services/kdevfullscreen.desktop
%{tde_prefix}/share/services/kdevg77options.desktop
%{tde_prefix}/share/services/kdevgccoptions.desktop
%{tde_prefix}/share/services/kdevgppoptions.desktop
%{tde_prefix}/share/services/kdevgrepview.desktop
%{tde_prefix}/share/services/kdevjavasupport.desktop
%{tde_prefix}/share/services/kdevtdeautoproject.desktop
%{tde_prefix}/share/services/kdevtdelibsimporter.desktop
%{tde_prefix}/share/services/kdevkonsoleview.desktop
%{tde_prefix}/share/services/kdevmakeview.desktop
%{tde_prefix}/share/services/kdevopenwith.desktop
%{tde_prefix}/share/services/kdevpartexplorer.desktop
%{tde_prefix}/share/services/kdevpascalproject.desktop
%{tde_prefix}/share/services/kdevpascalsupport.desktop
%{tde_prefix}/share/services/kdevpcscustomimporter.desktop
%{tde_prefix}/share/services/kdevperlsupport.desktop
%{tde_prefix}/share/services/kdevpgf77options.desktop
%{tde_prefix}/share/services/kdevpghpfoptions.desktop
%{tde_prefix}/share/services/kdevphpsupport.desktop
%{tde_prefix}/share/services/kdevpythonsupport.desktop
%{tde_prefix}/share/services/kdevqtimporter.desktop
%{tde_prefix}/share/services/kdevquickopen.desktop
%{tde_prefix}/share/services/kdevrbdebugger.desktop
%{tde_prefix}/share/services/kdevregexptest.desktop
%{tde_prefix}/share/services/kdevreplace.desktop
%{tde_prefix}/share/services/kdevrubysupport.desktop
%{tde_prefix}/share/services/kdevscripting.desktop
%{tde_prefix}/share/services/kdevscriptproject.desktop
%{tde_prefix}/share/services/kdevsnippet.desktop
%{tde_prefix}/share/services/kdevsqlsupport.desktop
%{tde_prefix}/share/services/kdevtexttools.desktop
%{tde_prefix}/share/services/kdevtipofday.desktop
%{tde_prefix}/share/services/kdevtmakeproject.desktop
%{tde_prefix}/share/services/kdevtools.desktop
%{tde_prefix}/share/services/kdevtrollproject.desktop
%{tde_prefix}/share/services/kdevuichooser.desktop
%{tde_prefix}/share/services/kdevvalgrind.desktop
%{tde_prefix}/share/services/kdevvcsmanager.desktop
%{tde_prefix}/share/services/perldoc.protocol
%{tde_prefix}/share/services/pydoc.protocol
%{tde_prefix}/share/servicetypes/tdevelopappfrontend.desktop
%{tde_prefix}/share/servicetypes/tdevelopcodebrowserfrontend.desktop
%{tde_prefix}/share/servicetypes/tdevelopcompileroptions.desktop
%{tde_prefix}/share/servicetypes/tdevelopcreatefile.desktop
%{tde_prefix}/share/servicetypes/tdevelopdifffrontend.desktop
%{tde_prefix}/share/servicetypes/tdevelopdocumentationplugins.desktop
%{tde_prefix}/share/servicetypes/tdeveloplanguagesupport.desktop
%{tde_prefix}/share/servicetypes/tdevelopmakefrontend.desktop
%{tde_prefix}/share/servicetypes/tdeveloppcsimporter.desktop
%{tde_prefix}/share/servicetypes/tdevelopplugin.desktop
%{tde_prefix}/share/servicetypes/tdevelopproject.desktop
%{tde_prefix}/share/servicetypes/tdevelopquickopen.desktop
%{tde_prefix}/share/servicetypes/tdevelopsourceformatter.desktop
%{tde_prefix}/share/servicetypes/tdevelopvcsintegrator.desktop
%{tde_prefix}/share/servicetypes/tdevelopversioncontrol.desktop
%{tde_prefix}/share/apps/kdevcsharpsupport/
%{tde_prefix}/share/apps/kdevctags2/
%{tde_prefix}/share/apps/kdevcustomproject/
%{tde_prefix}/share/apps/kdevdebugger/
%{tde_prefix}/share/apps/kdevdesigner/
%{tde_prefix}/share/apps/kdevdesignerpart/
%{tde_prefix}/share/apps/kdevdiff/
%{tde_prefix}/share/apps/kdevdistpart/
%{tde_prefix}/share/apps/kdevdocumentation/
%{tde_prefix}/share/apps/kdevdoxygen/
%{tde_prefix}/share/apps/tdevelop/
%{tde_prefix}/share/apps/kdevfilecreate/
%{tde_prefix}/share/apps/kdevfilelist/
%{tde_prefix}/share/apps/kdevfilter/
%{tde_prefix}/share/apps/kdevfortransupport/
%{tde_prefix}/share/apps/kdevfullscreen/
%{tde_prefix}/share/apps/kdevgrepview/
%{tde_prefix}/share/apps/kdevjavasupport/
%{tde_prefix}/share/apps/kdevmakeview/
%{tde_prefix}/share/apps/kdevpartexplorer/
%{tde_prefix}/share/apps/kdevpascalproject/
%{tde_prefix}/share/apps/kdevpascalsupport/
%{tde_prefix}/share/apps/kdevperlsupport/
%{tde_prefix}/share/apps/kdevphpsupport/
%{tde_prefix}/share/apps/kdevpythonsupport/
%{tde_prefix}/share/apps/kdevquickopen/
%{tde_prefix}/share/apps/kdevrbdebugger/
%{tde_prefix}/share/apps/kdevregexptest/
%{tde_prefix}/share/apps/kdevreplace/
%{tde_prefix}/share/apps/kdevrubysupport/
%{tde_prefix}/share/apps/kdevscripting/
%{tde_prefix}/share/apps/kdevscriptproject/
%{tde_prefix}/share/apps/kdevsnippet/
%{tde_prefix}/share/apps/kdevsqlsupport
%{tde_prefix}/share/apps/kdevtipofday/
%{tde_prefix}/share/apps/kdevtools/
%{tde_prefix}/share/apps/kdevtrollproject/
%{tde_prefix}/share/apps/kdevvalgrind/
%{tde_prefix}/share/apps/tdeio_pydoc/
%{tde_prefix}/share/desktop-directories/tde-development-tdevelop.directory
%{tde_prefix}/share/doc/tde/HTML/en/tdevelop/
%{tde_prefix}/%{_lib}/libd.so.0
%{tde_prefix}/%{_lib}/libd.so.0.0.0
%{tde_prefix}/%{_lib}/libkinterfacedesigner.so.0
%{tde_prefix}/%{_lib}/libkinterfacedesigner.so.0.0.0
%{tde_prefix}/%{_lib}/trinity/libkdevvisualboyadvance.la
%{tde_prefix}/%{_lib}/trinity/libkdevvisualboyadvance.so
%{tde_prefix}/share/apps/kdevvisualboyadvance/
%{tde_prefix}/share/doc/tde/HTML/en/tde_app_devel/
%{tde_prefix}/share/mimelnk/text/x-fortran.desktop
%{tde_prefix}/share/services/kdevvisualboyadvance.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kdevdesigner/

##########

%package devel
Summary: Development files for %{name}
Group:		Development/Libraries/Other
Requires: %{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdevelop-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdevelop-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development files for tdevelop.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/lib*.so
%{tde_prefix}/%{_lib}/lib*.la
%{tde_prefix}/include/*

##########

%package libs
Summary: %{name} runtime libraries
Group:   System Environment/Libraries
Requires: trinity-tdelibs >= %{tde_version}
# include to be paranoid, installing libs-only is still mostly untested -- Rex
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kdevelop-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdevelop-libs = %{?epoch:%{epoch}:}%{version}-%{release}

%description libs
This package contains the libraries needed for the tdevelop programs.

%files libs
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libdesignerintegration.so.0
%{tde_prefix}/%{_lib}/libdesignerintegration.so.0.0.0
%{tde_prefix}/%{_lib}/libdocumentation_interfaces.so.0
%{tde_prefix}/%{_lib}/libdocumentation_interfaces.so.0.0.0
%{tde_prefix}/%{_lib}/libgdbmi_parser.so.0
%{tde_prefix}/%{_lib}/libgdbmi_parser.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevbuildbase.so.0
%{tde_prefix}/%{_lib}/libkdevbuildbase.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevbuildtoolswidgets.so.0
%{tde_prefix}/%{_lib}/libkdevbuildtoolswidgets.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevcatalog.so.0
%{tde_prefix}/%{_lib}/libkdevcatalog.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevcppparser.so.0
%{tde_prefix}/%{_lib}/libkdevcppparser.so.0.0.0
%{tde_prefix}/%{_lib}/libtdevelop.so.1
%{tde_prefix}/%{_lib}/libtdevelop.so.1.0.0
%{tde_prefix}/%{_lib}/libkdevextras.so.0
%{tde_prefix}/%{_lib}/libkdevextras.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevpropertyeditor.so.0
%{tde_prefix}/%{_lib}/libkdevpropertyeditor.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevqmakeparser.so.0
%{tde_prefix}/%{_lib}/libkdevqmakeparser.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevshell.so.0
%{tde_prefix}/%{_lib}/libkdevshell.so.0.0.0
%{tde_prefix}/%{_lib}/libkdevwidgets.so.0
%{tde_prefix}/%{_lib}/libkdevwidgets.so.0.0.0
%{tde_prefix}/%{_lib}/liblang_debugger.so.0
%{tde_prefix}/%{_lib}/liblang_debugger.so.0.0.0
%{tde_prefix}/%{_lib}/liblang_interfaces.so.0
%{tde_prefix}/%{_lib}/liblang_interfaces.so.0.0.0
%{tde_prefix}/%{_lib}/libprofileengine.so.0
%{tde_prefix}/%{_lib}/libprofileengine.so.0.0.0


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"

%install -a
# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

