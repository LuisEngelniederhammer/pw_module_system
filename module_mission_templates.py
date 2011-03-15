from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
#
####################################################################################################################

mission_templates = [
  ("conquest", mtf_battle_mode, -1, "Fight for control of the castles.",
   [
    (0,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (1,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (2,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (3,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (4,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (5,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (6,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (7,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (8,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (9,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (10,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (11,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (12,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (13,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (14,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (15,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (16,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (17,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (18,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (19,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (20,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (21,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (22,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (23,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (24,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (25,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (26,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (27,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (28,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (29,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (30,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (31,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (32,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (33,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (34,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (35,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (36,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (37,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (38,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (39,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (40,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (41,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (42,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (43,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (44,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (45,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (46,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (47,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (48,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (49,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (50,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (51,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (52,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (53,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (54,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (55,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (56,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (57,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (58,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (59,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (60,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (61,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (62,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (63,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (64,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (65,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (66,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (67,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (68,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (69,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (70,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (71,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (72,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (73,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (74,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (75,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (76,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (77,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (78,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (79,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (80,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (81,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (82,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (83,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (84,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (85,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (86,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (87,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (88,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (89,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (90,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (91,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (92,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (93,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (94,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (95,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (96,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (97,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (98,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    (99,mtef_visitor_source,0,aif_start_alarmed,1,[]),
    ],
   [
    (ti_before_mission_start, 0, 0, [],
     [(server_set_friendly_fire, 1),
      (server_set_melee_friendly_fire, 1),
      (server_set_friendly_fire_damage_self_ratio, 0),
      (server_set_friendly_fire_damage_friend_ratio, 100),
      (team_set_relation, team_default, team_default, -1),
      (team_set_relation, team_default, team_spawn_invulnerable, 0),
      (team_set_relation, team_spawn_invulnerable, team_default, 0),
      (team_set_relation, team_spawn_invulnerable, team_spawn_invulnerable, 0),
      (call_script, "script_initialize_scene_globals"),
      (call_script, "script_scene_set_day_time"),
      (multiplayer_is_server),
      (call_script, "script_setup_owner_faction_for_castles"),
      (call_script, "script_setup_factions_for_scene"),
      (call_script, "script_setup_castle_money_chests"),
      (call_script, "script_setup_all_linked_scene_props"),
      ]),

    (ti_after_mission_start, 0, 0, [],
     [(set_spawn_effector_scene_prop_kind, 0, -1),
      (set_spawn_effector_scene_prop_kind, 1, -1),
      (assign, "$g_preset_message_display_enabled", 0),
      (multiplayer_is_server),
      (assign, "$g_next_scene", -1),
      (assign, "$g_next_mission", game_type_mission_templates_begin),
      (call_script, "script_setup_ship_collision_props"),
      (call_script, "script_setup_scene_props_after_mission_start"),
      (init_position, pos1),
      (set_spawn_position, pos1),
      (server_get_max_num_players, "$g_spawn_marker_count"),
      (val_add, "$g_spawn_marker_count", 1),
      (try_for_range, ":unused", 0, "$g_spawn_marker_count"),
        (spawn_scene_prop, "spr_spawn_marker"),
      (try_end),
      (assign, "$g_spawned_bot_count", 0),
      ]),

    (ti_server_player_joined, 0, 0, [],
     [(store_trigger_param_1, ":player_id"),
      (call_script, "script_setup_player_joined", ":player_id"),
      (multiplayer_is_server),
      (call_script, "script_player_check_name", ":player_id"),
      ]),

    (ti_on_agent_spawn, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (call_script, "script_on_agent_spawned", ":agent_id"),
      ]),

    (ti_on_agent_killed_or_wounded, 0, 0, [],
     [(store_trigger_param_1, ":dead_agent_id"),
      (store_trigger_param_2, ":killer_agent_id"),
      (call_script, "script_client_check_show_respawn_time_counter", ":dead_agent_id"),
      (call_script, "script_apply_consequences_for_agent_death", ":dead_agent_id", ":killer_agent_id"),
      (multiplayer_is_server),
      (call_script, "script_setup_agent_for_respawn", ":dead_agent_id"),
      (call_script, "script_check_spawn_bots", ":dead_agent_id"),
      ]),

    (ti_on_agent_hit, 0, 0, [],
     [(is_between, reg0, scripted_items_begin, scripted_items_end),
      (store_trigger_param_1, ":attacked_agent_id"),
      (store_trigger_param_2, ":attacker_agent_id"),
      (store_trigger_param_3, ":damage_dealt"),
      (call_script, "script_agent_hit_with_scripted_item", ":attacked_agent_id", ":attacker_agent_id", ":damage_dealt", reg0),
      ]),

    (ti_on_item_picked_up, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":item_id"),
      (store_trigger_param_3, ":instance_id"),
      (call_script, "script_check_on_item_picked_up", ":agent_id", ":item_id", ":instance_id"),
      ]),

    (ti_on_item_dropped, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":item_id"),
      (store_trigger_param_3, ":instance_id"),
      (call_script, "script_check_on_item_dropped", ":agent_id", ":item_id", ":instance_id", 0),
      ]),

    (ti_on_agent_mount, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":horse_agent_id"),
      (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
      (call_script, "script_check_agent_horse_speed_factor", ":agent_id", ":horse_agent_id"),
      ]),

    (ti_on_agent_dismount, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":horse_agent_id"),
      (agent_set_slot, ":horse_agent_id", slot_agent_horse_last_rider, ":agent_id"),
      ]),

    (0, 0, 0.1,
     [(multiplayer_is_server),
      (val_add, "$g_loop_player_id", 1),
      (get_max_players, ":max_players"),
      (try_begin),
        (ge, "$g_loop_player_id", ":max_players"),
        (assign, "$g_loop_player_id", 0),
        (store_mission_timer_a, ":time"),
        (try_begin),
          (ge, ":time", "$g_loop_player_check_time"),
          (val_add, "$g_loop_player_check_time", loop_player_check_interval),
          (assign, "$g_loop_player_check", 1),
        (else_try),
          (assign, "$g_loop_player_check", 0),
        (try_end),
        (try_begin),
          (ge, ":time", "$g_loop_player_check_outlaw_time"),
          (val_add, "$g_loop_player_check_outlaw_time", loop_player_check_outlaw_interval),
          (assign, "$g_loop_player_check_outlaw", 1),
        (else_try),
          (assign, "$g_loop_player_check_outlaw", 0),
        (try_end),
      (try_end),
      (try_begin),
        (gt, "$g_loop_player_id", 0),
        (assign, ":player_id", "$g_loop_player_id"),
        (try_begin),
          (eq, "$g_loop_player_check", 1),
          (try_begin),
            (player_is_active, ":player_id"),
            (call_script, "script_player_check_stored_values", ":player_id"),
          (else_try),
            (store_mul, ":player_index", ":player_id", player_array_entry_size),
            (neg|troop_slot_eq, "trp_active_players_array", ":player_index", 0),
            (call_script, "script_copy_player_values_to_inactive", ":player_index"),
            (troop_set_slot, "trp_active_players_array", ":player_index", 0),
          (try_end),
        (try_end),
        (player_is_active, ":player_id"),
        (call_script, "script_player_check_spawn_agent", ":player_id"),
        (try_begin),
          (eq, "$g_loop_player_check_outlaw", 1),
          (player_get_slot, ":outlaw_rating", ":player_id", slot_player_outlaw_rating),
          (try_begin),
            (gt, ":outlaw_rating", 0),
            (val_sub, ":outlaw_rating", 1),
            (player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
            (multiplayer_send_3_int_to_player, ":player_id", server_event_player_set_slot, ":player_id", slot_player_outlaw_rating, ":outlaw_rating"),
          (try_end),
        (try_end),
      (try_end),
      (eq, "$g_loop_player_id", 0),
      ], []),

    (30, 0, 0, [(multiplayer_is_server)],
     [(store_mission_timer_a, ":current_time"),
      (try_for_range, ":faction_id", factions_begin, factions_end),
        (faction_slot_ge,":faction_id", slot_faction_lord_player_uid, 1),
        (faction_get_slot, ":lord_last_seen_time", ":faction_id", slot_faction_lord_last_seen_time),
        (store_sub, ":lord_last_seen_interval", ":current_time", ":lord_last_seen_time"),
        (gt, ":lord_last_seen_interval", lord_wait_for_reconnect_interval),
        (faction_set_slot, ":faction_id", slot_faction_lord_player_uid, 0),
        (faction_set_slot, ":faction_id", slot_faction_lord_last_seen_time, 0),
      (try_end),
      ]),

    (0, 0, 0.1,
     [(multiplayer_is_server),
      (store_mission_timer_a, ":time"),
      (ge, ":time", "$g_loop_agent_check_time"),
      (assign, ":agent_id", -1),
      (try_for_agents, ":loop_agent_id"),
        (eq, ":agent_id", -1),
        (gt, ":loop_agent_id", "$g_loop_agent_last_checked"),
        (agent_is_active, ":loop_agent_id"),
        (assign, ":agent_id", ":loop_agent_id"),
      (try_end),
      (try_begin),
        (gt, ":agent_id", -1),
        (call_script, "script_check_agent_drowning", ":agent_id"),
        (try_begin),
          (eq, "$g_loop_horse_check", 1),
          (neg|agent_is_human, ":loop_agent_id"),
          (call_script, "script_check_remove_lost_horse", ":agent_id"),
        (try_end),
        (try_begin),
          (eq, "$g_loop_health_check", 1),
          (call_script, "script_check_agent_health", ":agent_id"),
        (try_end),
      (else_try),
        (val_add, "$g_loop_agent_check_time", loop_agent_check_interval),
        (try_begin),
          (ge, ":time", "$g_loop_horse_check_time"),
          (val_add, "$g_loop_horse_check_time", loop_horse_check_interval),
          (assign, "$g_loop_horse_check", 1),
        (else_try),
          (assign, "$g_loop_horse_check", 0),
        (try_end),
        (try_begin),
          (ge, ":time", "$g_loop_health_check_time"),
          (val_add, "$g_loop_health_check_time", loop_health_check_interval),
          (assign, "$g_loop_health_check", 1),
        (else_try),
          (assign, "$g_loop_health_check", 0),
        (try_end),
      (try_end),
      (assign, "$g_loop_agent_last_checked", ":agent_id"),
      (eq, ":agent_id", -1),
      ], []),

    (0, 0, 0, [(multiplayer_is_server)],
     [(troop_get_slot, ":ship_array_count", "trp_ship_array", slot_ship_array_count),
      (gt, ":ship_array_count", 0),
      (try_begin),
        (ge, "$g_loop_ship_to_check", slot_ship_array_begin),
        (troop_get_slot, ":hull_instance_id", "trp_ship_array", "$g_loop_ship_to_check"),
        (call_script, "script_move_ship", ":hull_instance_id"),
        (try_begin),
          (ge, "$g_loop_ship_to_check", ":ship_array_count"),
          (assign, "$g_loop_ship_to_check", 0),
        (else_try),
          (val_add, "$g_loop_ship_to_check", 1),
        (try_end),
      (else_try),
        (store_mission_timer_a, ":time"),
        (try_begin),
          (ge, ":time", "$g_loop_ship_check_time"),
          (val_add, "$g_loop_ship_check_time", 1),
          (val_sub, ":time", 1),
          (val_max, "$g_loop_ship_check_time", ":time"),
          (assign, "$g_loop_ship_to_check", slot_ship_array_begin),
        (try_end),
      (try_end),
      ]),

    (0, 0, 10,
     [(multiplayer_is_server),
      (troop_get_slot, ":resources_count", "trp_removed_scene_props", slot_removed_resources_count),
      (gt, ":resources_count", 0),
      (try_begin),
        (lt, "$g_loop_resource_to_check", ":resources_count"),
        (store_add, ":resource_slot", "$g_loop_resource_to_check", slot_removed_resources_begin),
        (troop_get_slot, ":instance_id", "trp_removed_scene_props", ":resource_slot"),
        (try_begin),
          (le, ":instance_id", 0),
        (else_try),
          (neg|scene_prop_slot_eq, ":instance_id", slot_scene_prop_state, scene_prop_state_hidden),
          (troop_set_slot, "trp_removed_scene_props", ":resource_slot", -1),
        (else_try),
          (scene_prop_get_slot, ":regen_time", ":instance_id", slot_scene_prop_state_time),
          (store_mission_timer_a, ":time"),
          (ge, ":time", ":regen_time"),
          (call_script, "script_regrow_resource", ":instance_id"),
          (troop_set_slot, "trp_removed_scene_props", ":resource_slot", -1),
        (try_end),
        (val_add, "$g_loop_resource_to_check", 1),
      (try_end),
      (ge, "$g_loop_resource_to_check", ":resources_count"),
      (assign, "$g_loop_resource_to_check", 0),
      ], []),

    (2, 0, 0, [(multiplayer_is_server)],
     [(call_script, "script_check_polls_ended"),
      ]),

    (1, 5, 0,
     [(multiplayer_is_server),
      (eq, "$g_game_ended", 0),
      (store_mission_timer_a, ":current_time"),
      (store_mul, ":game_end_time", "$g_map_time_limit", 60),
      (try_begin),
        (call_script, "script_cf_victory_condition_met"),
        (assign, ":faction_id", reg0),
        (try_begin),
          (le, "$g_victory_condition_time", 0),
          (store_mul, "$g_victory_condition_time", "$g_victory_condition", 60),
          (val_add, "$g_victory_condition_time", ":current_time"),
        (else_try),
          (gt, "$g_victory_condition_time", 0),
          (this_or_next|ge, ":current_time", "$g_victory_condition_time"),
          (ge, ":current_time", ":game_end_time"),
          (get_max_players, ":max_players"),
          (try_for_range, ":player_id", 1, ":max_players"),
            (player_is_active, ":player_id"),
            (multiplayer_send_3_int_to_player, ":player_id", server_event_preset_message, "str_s1_reign_supreme", preset_message_faction|preset_message_big|preset_message_log, ":faction_id"),
          (try_end),
          (assign, "$g_game_ended", 1),
        (try_end),
      (else_try),
        (assign, "$g_victory_condition_time", 0),
      (try_end),
      (this_or_next|eq, "$g_game_ended", 1),
      (this_or_next|is_between, "$g_next_scene", scenes_begin, scenes_end),
      (ge, ":current_time", ":game_end_time"),
      (assign, "$g_game_ended", 1),
      ],
     [(try_begin),
        (is_between, "$g_next_scene", scenes_begin, scenes_end),
        (start_multiplayer_mission, "$g_next_mission", "$g_next_scene", 1),
      (else_try),
        (start_multiplayer_mission, "$g_next_mission", 0, 0),
      (try_end),
      (call_script, "script_game_set_multiplayer_mission_end"),
      ]),

    (0, 0, redraw_castle_banners_interval, [(multiplayer_is_server)],
     [(call_script, "script_redraw_castle_banners", -1),
      ]),

    (ti_escape_pressed, 0, 0, [(call_script, "script_cf_no_input_presentation_active")],
     [(start_presentation, "prsnt_escape_menu"),
      ]),

    (ti_tab_pressed, 0, 0, [(call_script, "script_cf_no_input_presentation_active")],
     [(neg|is_presentation_active, "prsnt_stats_chart"),
      (assign, "$g_stats_chart_opened_manually", 1),
      (start_presentation, "prsnt_stats_chart"),
      ]),

    (ti_battle_window_opened, 0, 0, [],
     [(try_begin),
        (eq, "$g_display_agent_labels", 1),
        (start_presentation, "prsnt_display_agent_labels"),
      (try_end),
      (try_begin),
        (eq, "$g_display_chat_overlay", 1),
        (start_presentation, "prsnt_chat_overlay"),
      (try_end),
      (try_begin),
        (gt, "$g_respawn_start_time", 0),
        (start_presentation, "prsnt_respawn_time_counter"),
      (try_end),
      (start_presentation, "prsnt_gold"),
      ]),

    (0, 0, 0, [(game_key_clicked, gk_character_window),(call_script, "script_cf_no_input_presentation_active")],
     [(try_begin),
        (neg|is_presentation_active, "prsnt_display_agent_labels"),
        (assign, "$g_display_agent_labels", 1),
        (start_presentation, "prsnt_display_agent_labels"),
      (else_try),
        (assign, "$g_display_agent_labels", 0),
      (try_end),
      ]),

    (0, 0, 0, [(key_clicked, key_f7),(call_script, "script_cf_no_input_presentation_active")],
     [(try_begin),
        (eq, "$g_display_chat_overlay", 0),
        (assign, "$g_display_chat_overlay", 1),
        (start_presentation, "prsnt_chat_overlay"),
      (else_try),
        (assign, "$g_display_chat_overlay", 0),
      (try_end),
      ]),

    (0, 1, 1, [(key_clicked, key_slash),(call_script, "script_cf_no_input_presentation_active")],
     [(multiplayer_send_message_to_server, client_event_detach_scene_prop),
      ]),

    (0.3, 0.3, 0, [(troop_slot_eq, "trp_last_chat_message", slot_last_chat_message_not_recieved, 1)],
     [(troop_slot_eq, "trp_last_chat_message", slot_last_chat_message_not_recieved, 1),
      (troop_get_slot, ":event", "trp_last_chat_message", slot_last_chat_message_event_type),
      (try_begin),
        (ge, ":event", net_chat_type_multiplier),
        (multiplayer_send_int_to_server, client_event_chat_message_type, ":event"),
      (try_end),
      (val_and, ":event", net_chat_event_mask),
      (str_store_troop_name, s0, "trp_last_chat_message"),
      (multiplayer_send_string_to_server, ":event", s0),
      ]),

    (0, 0.05, 0, [(game_key_clicked, gk_quests_window),(call_script, "script_cf_no_input_presentation_active")],
     [(assign, "$g_chat_box_string_id", "str_send_message_to_players_nearby"),
      (assign, "$g_chat_box_event_type", chat_event_type_local),
      (start_presentation, "prsnt_chat_box"),
      ]),

    (0, 0.05, 0, [(game_key_clicked, gk_inventory_window),(call_script, "script_cf_no_input_presentation_active")],
     [(multiplayer_get_my_player, ":player_id"),
      (player_get_slot, ":faction_id", ":player_id", slot_player_faction_id),
      (is_between, ":faction_id", castle_factions_begin, factions_end),
      (str_store_faction_name, s11, ":faction_id"),
      (assign, "$g_chat_box_string_id", "str_send_message_to_the_s11"),
      (assign, "$g_chat_box_event_type", chat_event_type_faction),
      (start_presentation, "prsnt_chat_box"),
      ]),

    (0, 0.05, 0, [(game_key_clicked, gk_view_orders),(call_script, "script_cf_no_input_presentation_active")],
     [(try_begin),
        (multiplayer_get_my_player, ":player_id"),
        (player_is_admin, ":player_id"),
        (assign, "$g_chat_box_player_string_id", "str_send_admin_message_to_s1"),
      (else_try),
        (assign, "$g_chat_box_player_string_id", 0),
      (try_end),
      (assign, "$g_chat_box_string_id", "str_send_admin_message"),
      (assign, "$g_chat_box_event_type", chat_event_type_admin),
      (start_presentation, "prsnt_chat_box"),
      ]),

    (0, 0, 0,
     [(this_or_next|key_clicked, key_up),
      (this_or_next|key_clicked, key_down),
      (this_or_next|key_clicked, key_left),
      (key_clicked, key_right),
      (call_script, "script_cf_no_input_presentation_active")],
     [(call_script, "script_cf_client_check_control_ship"),
      ]),

    (0, 0, 0, [(game_key_clicked, gk_party_window),(call_script, "script_cf_no_input_presentation_active")],
     [(start_presentation, "prsnt_money_bag"),
      ]),

    (1, 0, ti_once, [(neg|multiplayer_is_server)],
     [(assign, "$g_preset_message_display_enabled", 1),
      ]),

    (0, 0, ti_once, [(neg|multiplayer_is_server)],
     [(str_store_welcome_message, s10),
      (call_script, "script_preset_message", "str_pw_welcome", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 4.0, [(neg|multiplayer_is_server)],
     [(call_script, "script_cf_turn_windmill_fans", 0),
      ]),

    (1, 0, 10,
     [(neg|multiplayer_is_server),
      (val_add, "$g_ambient_sound_instance_no", 1),
      (scene_prop_get_num_instances, ":num_instances", "spr_pw_scene_ambient_sound"),
      (try_begin),
        (ge, "$g_ambient_sound_instance_no", ":num_instances"),
        (assign, "$g_ambient_sound_instance_no", 0),
      (try_end),
      (scene_prop_get_instance, ":instance_id", "spr_pw_scene_ambient_sound", "$g_ambient_sound_instance_no"),
      (call_script, "script_cf_play_scene_ambient_sound", ":instance_id"),
      ], []),

    ]),

  ("edit_scene", 0, -1, "edit_scene", [(0,mtef_visitor_source,0,aif_start_alarmed,1,[])],
   [
    (ti_before_mission_start, 0, 0, [],
     [(server_set_add_to_game_servers_list, 0),
      (assign, "$g_edit_scene", 1),
      (call_script, "script_scene_set_day_time"),
      (call_script, "script_setup_castle_names"),
      ]),

    (ti_after_mission_start, 0, 0, [],
     [(set_spawn_effector_scene_prop_kind, team_default, -1),
      (team_set_relation, team_default, team_default, -1),
      (call_script, "script_initialize_troop_equipment_slots"),
      (call_script, "script_initialize_item_slots"),
      (call_script, "script_setup_ship_collision_props"),
      (display_message, "str_pw_editor_welcome"),
      ]),

    (ti_server_player_joined, 0, 0, [],
     [(store_trigger_param_1, ":player_id"),
      (player_set_team_no, ":player_id", team_default),
      (player_set_troop_id, ":player_id", "trp_player"),
      (entry_point_get_position, pos10, 0),
      (player_spawn_new_agent, ":player_id", 0),
      ]),

    (ti_on_agent_spawn, 0, 0, [],
     [(store_trigger_param_1, ":agent_id"),
      (neg|agent_is_non_player, ":agent_id"),
      (agent_set_position, ":agent_id", pos10),
      ]),

    (ti_escape_pressed, 0, 0, [],
     [(question_box, "str_leave_edit_mode"),
      ]),

    (ti_question_answered, 0, 0, [],
     [(store_trigger_param_1, ":answer"),
      (eq, ":answer", 0),
      (finish_mission),
      ]),

    (0, 0, 0, [(key_clicked, key_f1)],
     [(call_script, "script_preset_message", "str_pw_editor_info", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f2)],
     [(call_script, "script_preset_message", "str_pw_editor_values_info", preset_message_read_object, 0, 0),
      ]),

    (0, 0, 0, [(key_clicked, key_f12)],
     [(scene_prop_get_instance, ":instance_id", "spr_pw_test_gold", 0),
      (prop_instance_get_position, pos1, ":instance_id"),
      (get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos2, ":agent_id"),
      (get_distance_between_positions, reg1, pos1, pos2),
      (get_sq_distance_between_positions, reg2, pos1, pos2),
      (display_message, "str_distance_reg1_sq_distance_reg2"),
      ]),

    (0, 0, 0, [(key_clicked, key_f11)],
     [(get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_get_position, pos1, ":agent_id"),
      (position_move_x, 50),
      (set_spawn_position, pos1),
      (spawn_horse, "itm_test_horse"),
      ]),

    (0, 0, 0, [(key_clicked, key_f10)],
     [(troop_get_slot, ":collision_props_count", "trp_ship_array", slot_ship_array_collision_props_count),
      (try_begin),
        (ge, "$g_test_ship_collision_prop", ":collision_props_count"),
        (assign, "$g_test_ship_collision_prop", 0),
        (entry_point_get_position, pos1, 0),
      (else_try),
        (store_add, ":collision_prop_slot", slot_ship_array_collision_props_begin, "$g_test_ship_collision_prop"),
        (troop_get_slot, ":collision_instance_id", "trp_ship_array", ":collision_prop_slot"),
        (val_add, "$g_test_ship_collision_prop", 1),
        (prop_instance_get_position, pos1, ":collision_instance_id"),
      (try_end),
      (get_player_agent_no, ":agent_id"),
      (agent_is_active, ":agent_id"),
      (agent_is_alive, ":agent_id"),
      (agent_set_position, ":agent_id", pos1),
      ]),

    (0, 0, 0, [(key_clicked, key_f9)],
     [(multiplayer_get_my_player, ":player_id"),
      (player_get_agent_id, ":agent_id", ":player_id"),
      (try_begin),
        (agent_is_active, ":agent_id"),
        (agent_is_alive, ":agent_id"),
        (agent_fade_out, ":agent_id"),
        (try_for_range, ":player_equip_slot", slot_player_equip_item_0, slot_player_equip_end),
          (player_set_slot, ":player_id", ":player_equip_slot", 0),
        (try_end),
      (try_end),
      (store_random_in_range, ":troop_id", playable_troops_begin, playable_troops_end),
      (player_set_troop_id, ":player_id", ":troop_id"),
      (call_script, "script_player_add_default_troop_items", ":player_id", ":troop_id"),
      (call_script, "script_get_random_equipment", "itm_linen_tunic", "itm_tribal_warrior_outfit"),
      (player_set_slot, ":player_id", slot_player_equip_body, reg0),
      (call_script, "script_get_random_equipment", "itm_sarranid_boots_a", "itm_khergit_leather_boots"),
      (player_set_slot, ":player_id", slot_player_equip_foot, reg0),
      (call_script, "script_player_add_spawn_items", ":player_id", 1),
      (player_spawn_new_agent, ":player_id", 0),
      (mission_cam_get_position, pos10),
      ]),

    ]),
]
