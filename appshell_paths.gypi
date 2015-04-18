# Copyright (c) 2011 The Chromium Embedded Framework Authors. All rights
# reserved. Use of this source code is governed by a BSD-style license that
# can be found in the LICENSE file.

{
  'includes': [
    # Bring in the autogenerated source file lists.
    'deps/cef/cef_paths.gypi',
   ],
   'variables': {
    'includes_common': [
      'include/base/cef_atomic_ref_count.h',
      'include/base/cef_atomicops.h',
      'include/base/cef_basictypes.h',
      'include/base/cef_bind.h',
      'include/base/cef_bind_helpers.h',
      'include/base/cef_build.h',
      'include/base/cef_callback.h',
      'include/base/cef_callback_forward.h',
      'include/base/cef_callback_helpers.h',
      'include/base/cef_callback_list.h',
      'include/base/cef_cancelable_callback.h',
      'include/base/cef_lock.h',
      'include/base/cef_logging.h',
      'include/base/cef_macros.h',
      'include/base/cef_move.h',
      'include/base/cef_platform_thread.h',
      'include/base/cef_ref_counted.h',
      'include/base/cef_scoped_ptr.h',
      'include/base/cef_string16.h',
      'include/base/cef_template_util.h',
      'include/base/cef_thread_checker.h',
      'include/base/cef_thread_collision_warner.h',
      'include/base/cef_trace_event.h',
      'include/base/cef_tuple.h',
      'include/base/cef_weak_ptr.h',
      'include/base/internal/cef_bind_internal.h',
      'include/base/internal/cef_callback_internal.h',
      'include/base/internal/cef_lock_impl.h',
      'include/base/internal/cef_raw_scoped_refptr_mismatch_checker.h',
      'include/base/internal/cef_thread_checker_impl.h',
      'include/cef_base.h',
      'include/cef_pack_resources.h',
      'include/cef_pack_strings.h',
      'include/cef_runnable.h',
      'include/cef_version.h',
      'include/internal/cef_export.h',
      'include/internal/cef_logging_internal.h',
      'include/internal/cef_ptr.h',
      'include/internal/cef_string.h',
      'include/internal/cef_string_list.h',
      'include/internal/cef_string_map.h',
      'include/internal/cef_string_multimap.h',
      'include/internal/cef_string_types.h',
      'include/internal/cef_string_wrappers.h',
      'include/internal/cef_thread_internal.h',
      'include/internal/cef_time.h',
      'include/internal/cef_trace_event_internal.h',
      'include/internal/cef_types.h',
      'include/internal/cef_types_wrappers.h',
      '<@(autogen_cpp_includes)',
    ],
    'includes_capi': [
      'include/capi/cef_base_capi.h',
      '<@(autogen_capi_includes)',
    ],
    'includes_wrapper': [
      'include/wrapper/cef_byte_read_handler.h',
      'include/wrapper/cef_closure_task.h',
      'include/wrapper/cef_helpers.h',
      'include/wrapper/cef_message_router.h',
      'include/wrapper/cef_stream_resource_handler.h',
      'include/wrapper/cef_xml_object.h',
      'include/wrapper/cef_zip_archive.h',

    ],
    'includes_win': [
      'include/base/internal/cef_atomicops_x86_msvc.h',
      'include/base/internal/cef_bind_internal_win.h',
      'include/cef_sandbox_win.h',
      'include/internal/cef_types_win.h',
      'include/internal/cef_win.h',
    ],
    'includes_mac': [
      'include/base/internal/cef_atomicops_atomicword_compat.h',
      'include/base/internal/cef_atomicops_mac.h',
      'include/cef_application_mac.h',
      'include/internal/cef_mac.h',
      'include/internal/cef_types_mac.h',
    ],
    'includes_linux': [
      'include/base/internal/cef_atomicops_atomicword_compat.h',
      'include/base/internal/cef_atomicops_x86_gcc.h',
      'include/internal/cef_linux.h',
      'include/internal/cef_types_linux.h',
    ],
    'libcef_sources_common': [
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/libcef_dll.cc',
      'libcef_dll/libcef_dll2.cc',
      'libcef_dll/resource.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      '<@(autogen_library_side)',
    ],
    'libcef_dll_wrapper_sources_common': [
      'libcef_dll/base/cef_atomicops_x86_gcc.cc',
      'libcef_dll/base/cef_bind_helpers.cc',
      'libcef_dll/base/cef_callback_helpers.cc',
      'libcef_dll/base/cef_callback_internal.cc',
      'libcef_dll/base/cef_lock.cc',
      'libcef_dll/base/cef_lock_impl.cc',
      'libcef_dll/base/cef_logging.cc',
      'libcef_dll/base/cef_ref_counted.cc',
      'libcef_dll/base/cef_string16.cc',
      'libcef_dll/base/cef_thread_checker_impl.cc',
      'libcef_dll/base/cef_thread_collision_warner.cc',
      'libcef_dll/base/cef_weak_ptr.cc',
      'libcef_dll/cpptoc/base_cpptoc.h',
      'libcef_dll/cpptoc/cpptoc.h',
      'libcef_dll/ctocpp/base_ctocpp.h',
      'libcef_dll/ctocpp/ctocpp.h',
      'libcef_dll/transfer_util.cpp',
      'libcef_dll/transfer_util.h',
      'libcef_dll/wrapper/cef_browser_info_map.h',
      'libcef_dll/wrapper/cef_byte_read_handler.cc',
      'libcef_dll/wrapper/cef_closure_task.cc',
      'libcef_dll/wrapper/cef_message_router.cc',
      'libcef_dll/wrapper/cef_stream_resource_handler.cc',
      'libcef_dll/wrapper/cef_xml_object.cc',
      'libcef_dll/wrapper/cef_zip_archive.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper.cc',
      'libcef_dll/wrapper/libcef_dll_wrapper2.cc',
      '<@(autogen_client_side)',
    ],
    'appshell_sources_common': [
      'appshell/appshell_extensions.cpp',
      'appshell/appshell_extensions.h',
      'appshell/appshell_extensions_platform.h',
      'appshell/appshell_extensions.js',
      'appshell/appshell_node_process.h',
      'appshell/appshell_node_process_internal.h',
      'appshell/appshell_node_process.cpp',
      'appshell/command_callbacks.h',
      'appshell/config.h',
      'appshell/cefclient.cpp',
      'appshell/cefclient.h',
      'appshell/client_app.cpp',
      'appshell/client_app.h',
      'appshell/client_app_delegates.cpp',
      'appshell/client_handler.cpp',
      'appshell/client_handler.h',
      'appshell/client_switches.cpp',
      'appshell/client_switches.h',
      'appshell/native_menu_model.cpp',
      'appshell/native_menu_model.h',
      'appshell/resource_util.h',
      'appshell/string_util.cpp',
      'appshell/string_util.h',
      'appshell/util.h',
    ],
    'appshell_sources_win': [
      'appshell/appshell_extensions_win.cpp',
      'appshell/appshell_node_process_win.cpp',
      'appshell/cefclient.rc',
      'appshell/version.rc',
      'appshell/cefclient_win.cpp',
      'appshell/client_app_win.cpp',
      'appshell/client_handler_win.cpp',
      'appshell/resource.h',
      'appshell/res/appshell.ico',
      'appshell/resource_util_win.cpp',
      'appshell/cef_buffered_dc.h',
      'appshell/cef_dark_aero_window.cpp',
      'appshell/cef_dark_aero_window.h',
      'appshell/cef_dark_window.cpp',
      'appshell/cef_dark_window.h',
      'appshell/cef_host_window.cpp',
      'appshell/cef_host_window.h',
      'appshell/cef_main_window.cpp',
      'appshell/cef_main_window.h',
      'appshell/cef_popup_window.cpp',
      'appshell/cef_popup_window.h',
      'appshell/cef_registry.cpp',
      'appshell/cef_registry.h',
      'appshell/cef_window.cpp',
      'appshell/cef_window.h',
      'appshell/res/close-hover.png',
      'appshell/res/close.png',
      'appshell/res/max-hover.png',
      'appshell/res/max.png',
      'appshell/res/min-hover.png',
      'appshell/res/min.png',
      'appshell/res/restore-hover.png',
      'appshell/res/restore.png',
      'appshell/res/close-pressed.png',
      'appshell/res/max-pressed.png',
      'appshell/res/min-pressed.png',
      'appshell/res/restore-pressed.png',
    ],
    'appshell_sources_mac': [
      'appshell/client_colors_mac.h',
      'appshell/TrafficLightButton.h',
      'appshell/TrafficLightButton.mm',
      'appshell/TrafficLightsView.h',
      'appshell/TrafficLightsView.mm',
      'appshell/TrafficLightsViewController.h',
      'appshell/TrafficLightsViewController.mm',
      'appshell/CustomTitlebarView.h',
      'appshell/CustomTitlebarView.m',
      'appshell/FullScreenButton.h',
      'appshell/FullScreenButton.mm',
      'appshell/FullScreenView.h',
      'appshell/FullScreenView.mm',
      'appshell/FullScreenViewController.h',
      'appshell/FullScreenViewController.mm',     
      'appshell/appshell_extensions_mac.mm',
      'appshell/appshell_node_process_mac.mm',
      'appshell/client_app_mac.mm',
      'appshell/cefclient_mac.mm',
      'appshell/client_handler_mac.mm',
      'appshell/resource_util_mac.mm',
    ],
    'appshell_sources_linux': [
      'appshell/appshell_extensions_gtk.cpp',
      'appshell/appshell_node_process_linux.cpp',
      'appshell/client_app_gtk.cpp',
      'appshell/cefclient_gtk.cpp',
      'appshell/client_handler_gtk.cpp',
      'appshell/resource_util_linux.cpp',
    ],
    'appshell_sources_mac_helper': [
      'appshell/TrafficLightButton.h',
      'appshell/TrafficLightButton.mm',
      'appshell/TrafficLightsView.h',
      'appshell/TrafficLightsView.mm',
      'appshell/TrafficLightsViewController.h',
      'appshell/TrafficLightsViewController.mm',
      'appshell/CustomTitlebarView.h',
      'appshell/CustomTitlebarView.m',
      'appshell/FullScreenButton.h',
      'appshell/FullScreenButton.mm',
      'appshell/FullScreenView.h',
      'appshell/FullScreenView.mm',
      'appshell/FullScreenViewController.h',
      'appshell/FullScreenViewController.mm',     
      'appshell/appshell_extensions.cpp',
      'appshell/appshell_extensions.h',
      'appshell/appshell_extensions_mac.mm',
      'appshell/appshell_node_process.h',
      'appshell/appshell_node_process_internal.h',
      'appshell/appshell_node_process.cpp',
      'appshell/appshell_node_process_mac.mm',
      'appshell/client_app.cpp',
      'appshell/client_app.h',
      'appshell/client_app_mac.mm',
      'appshell/client_app_delegates.cpp',
      'appshell/client_handler.cpp',
      'appshell/client_handler.h',
      'appshell/client_handler_mac.mm',
      'appshell/client_switches.cpp',
      'appshell/client_switches.h',
      'appshell/native_menu_model.cpp',
      'appshell/native_menu_model.h',
      'appshell/process_helper_mac.cpp',
      'appshell/resource_util.h',
      'appshell/resource_util_mac.mm',
      'appshell/string_util.cpp',
      'appshell/string_util.h',
      'appshell/util.h',
    ],
    'appshell_bundle_resources_mac': [
      'appshell/mac/appshell.icns',
      'appshell/mac/English.lproj/InfoPlist.strings',
      'appshell/mac/English.lproj/MainMenu.xib',
      'appshell/mac/TrafficLights.xib',
      'appshell/mac/FullScreen.xib',
      'appshell/mac/French.lproj/InfoPlist.strings',
      'appshell/mac/French.lproj/MainMenu.xib',
      'appshell/mac/Japanese.lproj/InfoPlist.strings',
      'appshell/mac/Japanese.lproj/MainMenu.xib',
      'appshell/mac/Info.plist',
      'appshell/appshell_extensions.js',
      'appshell/mac/brackets.sh',
      'appshell/mac/window-close-active.png',
      'appshell/mac/window-close-active@2x.png',
      'appshell/mac/window-close-dirty-active.png',
      'appshell/mac/window-close-dirty-active@2x.png',
      'appshell/mac/window-close-dirty-hover.png',
      'appshell/mac/window-close-dirty-hover@2x.png',
      'appshell/mac/window-close-dirty-inactive.png',
      'appshell/mac/window-close-dirty-inactive@2x.png',
      'appshell/mac/window-close-dirty-pressed.png',
      'appshell/mac/window-close-dirty-pressed@2x.png',
      'appshell/mac/window-close-hover.png',
      'appshell/mac/window-close-hover@2x.png',
      'appshell/mac/window-close-inactive.png',
      'appshell/mac/window-close-inactive@2x.png',
      'appshell/mac/window-close-pressed.png',
      'appshell/mac/window-close-pressed@2x.png',
      'appshell/mac/window-minimize-active.png',
      'appshell/mac/window-minimize-active@2x.png',
      'appshell/mac/window-minimize-hover.png',
      'appshell/mac/window-minimize-hover@2x.png',
      'appshell/mac/window-minimize-inactive.png',
      'appshell/mac/window-minimize-inactive@2x.png',
      'appshell/mac/window-minimize-pressed.png',
      'appshell/mac/window-minimize-pressed@2x.png',
      'appshell/mac/window-zoom-active.png',
      'appshell/mac/window-zoom-active@2x.png',
      'appshell/mac/window-zoom-hover.png',
      'appshell/mac/window-zoom-hover@2x.png',
      'appshell/mac/window-zoom-inactive.png',
      'appshell/mac/window-zoom-inactive@2x.png',
      'appshell/mac/window-zoom-pressed.png',
      'appshell/mac/window-zoom-pressed@2x.png',
      'appshell/mac/window-fullscreen-pressed.png',
      'appshell/mac/window-fullscreen-pressed@2x.png',
      'appshell/mac/window-fullscreen-hover.png',
      'appshell/mac/window-fullscreen-hover@2x.png',
      'appshell/mac/window-fullscreen-active.png',
      'appshell/mac/window-fullscreen-active@2x.png',
      'appshell/mac/window-fullscreen-inactive.png',
      'appshell/mac/window-fullscreen-inactive@2x.png',
    ],
    'appshell_bundle_resources_linux': [
      'Resources/locales',
      'appshell/res/appshell32.png',
      'appshell/res/appshell48.png',
      'appshell/res/appshell128.png',
      'appshell/res/appshell256.png',
      'Resources/cef.pak',
      'Resources/devtools_resources.pak',
    ],
    'appshell_bundle_libraries_linux': [
      '$(BUILDTYPE)/libcef.so',
    ],
  },
}
