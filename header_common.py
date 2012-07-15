###################################################
# header_common.py
# This file contains common declarations.
# DO NOT EDIT THIS FILE!
###################################################

server_event_preset_message                     = 0
server_event_play_sound                         = 1
server_event_scene_prop_play_sound              = 2
server_event_play_sound_at_position             = 3
server_event_agent_equip_armor                  = 4
server_event_player_set_slot                    = 5
server_event_scene_prop_set_slot                = 6
server_event_faction_set_slot                   = 7
server_event_troop_set_slot                     = 8
server_event_agent_set_slot                     = 9
server_event_show_inventory                     = 10
server_event_chat_message_recieved              = 11
server_event_local_chat                         = 12
server_event_local_chat_shout                   = 13
server_event_faction_set_name                   = 14
server_event_return_game_rules                  = 15
server_event_return_server_name                 = 16
server_event_return_password                    = 17
server_event_set_player_score_kill_death        = 18
server_event_show_poll                          = 19
server_event_set_overflow_gold                  = 20
server_event_faction_chat                       = 21
server_event_faction_lord_chat                  = 22
server_event_admin_chat                         = 23
server_event_admin_chat_shout                   = 24
server_event_admin_set_permissions              = 25
server_event_set_attached_scene_prop            = 26

client_event_reveal_money_pouch                 = 96
client_event_agent_loot_armor                   = 97
client_event_toggle_drop_armor                  = 98
client_event_admin_equip_item                   = 99
client_event_poll_vote                          = 100
client_event_request_poll                       = 101
client_event_request_spawn_point                = 102
client_event_request_game_rules                 = 103
client_event_admin_set_server_name              = 104
client_event_admin_set_password                 = 105
client_event_admin_set_welcome_message          = 106
client_event_admin_set_game_rule                = 107
client_event_admin_action                       = 108
client_event_faction_admin_action               = 109
client_event_chat_message_begin                 = 110
client_event_chat_message_end                   = 120
client_event_chat_message_type                  = 120
client_event_transfer_gold                      = 121
client_event_request_stock_count                = 122
client_event_drop_money_bag                     = 123
client_event_change_faction_banner              = 124
client_event_transfer_inventory                 = 125
client_event_control_scene_prop                 = 126
client_event_attach_scene_prop                  = 127

preset_message_default                          = 0x0
preset_message_item                             = 0x2
preset_message_agent                            = 0x3
preset_message_player                           = 0x4
preset_message_faction                          = 0x5
preset_message_faction_castle                   = 0x6
preset_message_params_mask                      = 0xF

preset_message_white                            = 0x00
preset_message_red                              = 0x10
preset_message_green                            = 0x20
preset_message_blue                             = 0x30
preset_message_yellow                           = 0x40
preset_message_color_mask                       = 0xF0

preset_message_small                            = 0x000
preset_message_big                              = 0x100
preset_message_read_object                      = 0x200
preset_message_chat_only                        = 0x300
preset_message_type_mask                        = 0xF00

preset_message_log                              = 0x1000
preset_message_fail_sound                       = 0x2000

preset_message_error                            = preset_message_red|preset_message_fail_sound
preset_message_info                             = preset_message_yellow
preset_message_chat_log                         = preset_message_chat_only|preset_message_log

# Module system commands
command_get_bot_count                           = 1
command_set_bot_count                           = 2
command_get_round_max_seconds                   = 3
command_set_round_max_seconds                   = 4
command_get_respawn_period                      = 5
command_set_respawn_period                      = 6
command_get_num_bots_voteable                   = 7
command_set_num_bots_voteable                   = 8
command_get_maps_voteable                       = 9
command_set_maps_voteable                       = 10
command_get_factions_voteable                   = 11
command_set_factions_voteable                   = 12
command_get_player_respawn_as_bot               = 13
command_set_player_respawn_as_bot               = 14
command_get_kick_voteable                       = 15
command_set_kick_voteable                       = 16
command_get_ban_voteable                        = 17
command_set_ban_voteable                        = 18
command_get_valid_vote_ratio                    = 19
command_set_valid_vote_ratio                    = 20
command_get_auto_team_balance_limit             = 21
command_set_auto_team_balance_limit             = 22
command_get_starting_gold                       = 23
command_set_starting_gold                       = 24
command_get_combat_gold_bonus                   = 25
command_set_combat_gold_bonus                   = 26
command_get_round_gold_bonus                    = 27
command_set_round_gold_bonus                    = 28
command_get_player_banners_allowed              = 29
command_set_player_banners_allowed              = 30
command_get_force_default_armor                 = 31
command_set_force_default_armor                 = 32
command_get_team_points_gained_for_flags        = 33
command_set_team_points_gained_for_flags        = 34
command_get_points_gained_for_capturing_flags   = 35
command_set_points_gained_for_capturing_flags   = 36
command_get_map_time_limit                      = 37
command_set_map_time_limit                      = 38
command_get_team_point_limit                    = 39
command_set_team_point_limit                    = 40
command_get_defender_spawn_count                = 41
command_set_defender_spawn_count                = 42
command_get_disallow_ranged_weapons             = 43
command_set_disallow_ranged_weapons             = 44
# Napoleonic Wars commands
command_use_class_limits                        = 50
command_class_limit_player_count                = 51
command_squad_size                              = 52
command_scale_squad                             = 53
command_build_points_team1                      = 54
command_build_points_team2                      = 55
command_allow_multiple_firearms                 = 56
command_enable_bonuses                          = 57
command_bonus_strength                          = 58
command_bonus_range                             = 59
command_fall_off_horse                          = 60
command_horse_dying                             = 61
command_auto_kick                               = 62
command_max_teamkills_before_kick               = 63
command_auto_horse                              = 64
command_auto_swap                               = 65
command_limit_grenadier                         = 66
command_limit_skirmisher                        = 67
command_limit_rifle                             = 68
command_limit_cavalry                           = 69
command_limit_lancer                            = 70
command_limit_hussar                            = 71
command_limit_dragoon                           = 72
command_limit_cuirassier                        = 73
command_limit_heavycav                          = 74
command_limit_artillery                         = 75
command_limit_rocket                            = 76
command_limit_sapper                            = 77
command_limit_musician                          = 78
command_limit_sergeant                          = 79
command_limit_officer                           = 80
command_limit_general                           = 81
# Hard coded commands
command_get_max_players                         = 101
command_set_max_players                         = 102
command_get_friendly_fire                       = 103
command_set_friendly_fire                       = 104
command_get_melee_friendly_fire                 = 105
command_set_melee_friendly_fire                 = 106
command_get_friendly_fire_damage_self_ratio     = 107
command_set_friendly_fire_damage_self_ratio     = 108
command_get_friendly_fire_damage_friend_ratio   = 109
command_set_friendly_fire_damage_friend_ratio   = 110
command_get_ghost_mode                          = 111
command_set_ghost_mode                          = 112
command_get_control_block_direction             = 113
command_set_control_block_direction             = 114
command_get_combat_speed                        = 115
command_set_combat_speed                        = 116
command_get_add_to_game_servers_list            = 117
command_set_add_to_game_servers_list            = 118
command_get_anti_cheat                          = 119
command_set_anti_cheat                          = 120
command_get_renaming_server_allowed             = 121
command_set_renaming_server_allowed             = 122
command_get_changing_game_type_allowed          = 123
command_set_changing_game_type_allowed          = 124
command_start_scene                             = 130
command_open_admin_panel                        = 132
command_open_game_rules                         = 134
command_set_server_mission_timer                = 136

commands_module_system_begin                    = command_get_bot_count
commands_module_system_end                      = command_set_disallow_ranged_weapons + 1
commands_napoleonic_wars_begin                  = command_use_class_limits
commands_napoleonic_wars_end                    = command_limit_general + 1
commands_hard_coded_begin                       = command_get_max_players
commands_hard_coded_end                         = command_set_anti_cheat + 1

min_num_players                                 = 2
max_num_players                                 = 250
min_respawn_period                              = 3
max_respawn_period                              = 31

net_value_upper_bound = 1 << 31
net_sound_shift = 16
net_sound_mask = (1 << net_sound_shift) - 1

net_pack_3_shift_2 = 10
net_pack_3_shift_3 = 20
net_pack_3_value_upper_bound = 1 << net_pack_3_shift_2
net_pack_3_mask_1 = net_pack_3_value_upper_bound - 1
net_pack_3_mask_2 = net_pack_3_mask_1 << net_pack_3_shift_2
net_pack_3_mask_3 = net_pack_3_mask_1 << net_pack_3_shift_3

net_chat_type_shift = 8
net_chat_param_1_shift = net_chat_type_shift * 2
net_chat_event_mask = (1 << net_chat_type_shift) - 1

stats_chart_score_shift = 8
stats_chart_ranking_shift = 24
stats_chart_score_max = 1 << (stats_chart_ranking_shift - stats_chart_score_shift)
stats_chart_player_mask = (1 << stats_chart_score_shift) - 1

admin_action_kick_player                        = 0
admin_action_ban_player_temp                    = 1
admin_action_ban_player_perm                    = 2
admin_action_mute_player                        = 3
admin_action_kill_player                        = 4
admin_action_fade_player_out                    = 5
admin_action_freeze_player                      = 6
admin_action_teleport_to_player                 = 7
admin_action_teleport_behind_player             = 8
admin_action_teleport_forwards                  = 9
admin_action_get_armor                          = 10
admin_action_get_invisible                      = 11
admin_action_refill_health                      = 12
admin_action_become_godlike                     = 13
admin_action_get_horse                          = 14
admin_action_remove_horses                      = 15
admin_action_remove_stray_horses                = 16
admin_action_teleport_to_ships                  = 17
admin_action_reset_ships                        = 18
admin_action_lock_faction                       = 19

faction_admin_action_change_banner              = 0
faction_admin_action_kick_player                = 1
faction_admin_action_toggle_player_door_key     = 2
faction_admin_action_toggle_player_money_key    = 3
faction_admin_action_toggle_player_item_key     = 4
faction_admin_action_set_relation_hostile       = 5
faction_admin_action_set_relation_peaceful      = 6
faction_admin_action_outlaw_player              = 7
faction_admin_action_mute_player                = 8

max_possible_gold                               = 1000000000
max_correctly_displayed_gold                    = 131071
max_correctly_displayed_hp                      = 15000


bignum = 0x40000000000000000000000000000000

op_num_value_bits = 24 + 32

tag_register        =  1
tag_variable        =  2
tag_string          =  3
tag_item            =  4
tag_troop           =  5
tag_faction         =  6
tag_quest           =  7
tag_party_tpl       =  8
tag_party           =  9
tag_scene           = 10
tag_mission_tpl     = 11
tag_menu            = 12
tag_script          = 13
tag_particle_sys    = 14
tag_scene_prop      = 15
tag_sound           = 16
tag_local_variable  = 17
tag_map_icon        = 18
tag_skill           = 19
tag_mesh            = 20
tag_presentation    = 21
tag_quick_string    = 22
tag_track           = 23
tag_tableau         = 24
tag_animation       = 25
tags_end            = 26

opmask_register             =  tag_register       << op_num_value_bits
opmask_variable             =  tag_variable       << op_num_value_bits
opmask_string               =  tag_string         << op_num_value_bits
opmask_item_index           =  tag_item           << op_num_value_bits
opmask_troop_index          =  tag_troop          << op_num_value_bits
opmask_faction_index        =  tag_faction        << op_num_value_bits
opmask_quest_index          =  tag_quest          << op_num_value_bits
opmask_p_template_index     =  tag_party_tpl      << op_num_value_bits
opmask_party_index          =  tag_party          << op_num_value_bits
opmask_scene_index          =  tag_scene          << op_num_value_bits
opmask_mission_tpl_index    =  tag_mission_tpl    << op_num_value_bits
opmask_menu_index           =  tag_menu           << op_num_value_bits
opmask_script               =  tag_script         << op_num_value_bits
opmask_particle_sys         =  tag_particle_sys   << op_num_value_bits
opmask_scene_prop           =  tag_scene_prop     << op_num_value_bits
opmask_sound                =  tag_sound          << op_num_value_bits
opmask_map_icon             =  tag_map_icon       << op_num_value_bits
opmask_local_variable       =  tag_local_variable << op_num_value_bits
opmask_quick_string         =  tag_quick_string   << op_num_value_bits


def reg(reg_no):
  if not 0 < reg_no < 128:
    raise Exception("ERROR: invalid register number.")
  return opmask_register | reg_no

s0 =  0
s1 =  1
s2 =  2
s3 =  3
s4 =  4
s5 =  5
s6 =  6
s7 =  7
s8 =  8
s9 =  9
s10 = 10
s11 = 11
s12 = 12
s13 = 13
s14 = 14
s15 = 15
s16 = 16
s17 = 17
s18 = 18
s19 = 19
s20 = 20
s21 = 21
s22 = 22
s23 = 23
s24 = 24
s25 = 25
s26 = 26
s27 = 27
s28 = 28
s29 = 29
s30 = 30
s31 = 31
s32 = 32
s33 = 33
s34 = 34
s35 = 35
s36 = 36
s37 = 37
s38 = 38
s39 = 39
s40 = 40
s41 = 41
s42 = 42
s43 = 43
s44 = 44
s45 = 45
s46 = 46
s47 = 47
s48 = 48
s49 = 49
s50 = 50
s51 = 51
s52 = 52
s53 = 53
s54 = 54
s55 = 55
s56 = 56
s57 = 57
s58 = 58
s59 = 59
s60 = 60
s61 = 61
s62 = 62
s63 = 63
s64 = 64
s65 = 65
s66 = 66
s67 = 67
s68 = 68
s69 = 69
s70 = 70
s71 = 71
s72 = 72
s73 = 73
s74 = 74
s75 = 75
s76 = 76
s77 = 77
s78 = 78
s79 = 79
s80 = 80
s81 = 81
s82 = 82
s83 = 83
s84 = 84
s85 = 85
s86 = 86
s87 = 87
s88 = 88
s89 = 89
s90 = 90
s91 = 91
s92 = 92
s93 = 93
s94 = 94
s95 = 95
s96 = 96
s97 = 97
s98 = 98
s99 = 99
s100 = 100
s101 = 101
s102 = 102
s103 = 103
s104 = 104
s105 = 105
s106 = 106
s107 = 107
s108 = 108
s109 = 109
s110 = 110
s111 = 111
s112 = 112
s113 = 113
s114 = 114
s115 = 115
s116 = 116
s117 = 117
s118 = 118
s119 = 119
s120 = 120
s121 = 121
s122 = 122
s123 = 123
s124 = 124
s125 = 125
s126 = 126
s127 = 127

pos0 =  0
pos1 =  1
pos2 =  2
pos3 =  3
pos4 =  4
pos5 =  5
pos6 =  6
pos7 =  7
pos8 =  8
pos9 =  9
pos10 = 10
pos11 = 11
pos12 = 12
pos13 = 13
pos14 = 14
pos15 = 15
pos16 = 16
pos17 = 17
pos18 = 18
pos19 = 19
pos20 = 20
pos21 = 21
pos22 = 22
pos23 = 23
pos24 = 24
pos25 = 25
pos26 = 26
pos27 = 27
pos28 = 28
pos29 = 29
pos30 = 30
pos31 = 31
pos32 = 32
pos33 = 33
pos34 = 34
pos35 = 35
pos36 = 36
pos37 = 37
pos38 = 38
pos39 = 39
pos40 = 40
pos41 = 41
pos42 = 42
pos43 = 43
pos44 = 44
pos45 = 45
pos46 = 46
pos47 = 47
pos48 = 48
pos49 = 49
pos50 = 50
pos51 = 51
pos52 = 52
pos53 = 53
pos54 = 54
pos55 = 55
pos56 = 56
pos57 = 57
pos58 = 58
pos59 = 59
pos60 = 60
pos61 = 61
pos62 = 62
pos63 = 63
pos64 = 64
pos65 = 65
pos66 = 66
pos67 = 67
pos68 = 68
pos69 = 69
pos70 = 70
pos71 = 71
pos72 = 72
pos73 = 73
pos74 = 74
pos75 = 75
pos76 = 76
pos77 = 77
pos78 = 78
pos79 = 79
pos80 = 80
pos81 = 81
pos82 = 82
pos83 = 83
pos84 = 84
pos85 = 85
pos86 = 86
pos87 = 87
pos88 = 88
pos89 = 89
pos90 = 90
pos91 = 91
pos92 = 92
pos93 = 93
pos94 = 94
pos95 = 95
pos96 = 96
pos97 = 97
pos98 = 98
pos99 = 99
pos100 = 100
pos101 = 101
pos102 = 102
pos103 = 103
pos104 = 104
pos105 = 105
pos106 = 106
pos107 = 107
pos108 = 108
pos109 = 109
pos110 = 110
pos111 = 111
pos112 = 112
pos113 = 113
pos114 = 114
pos115 = 115
pos116 = 116
pos117 = 117
pos118 = 118
pos119 = 119
pos120 = 120
pos121 = 121
pos122 = 122
pos123 = 123
pos124 = 124
pos125 = 125
pos126 = 126
pos127 = 127

reg0 = opmask_register| 0
reg1 = opmask_register| 1
reg2 = opmask_register| 2
reg3 = opmask_register| 3
reg4 = opmask_register| 4
reg5 = opmask_register| 5
reg6 = opmask_register| 6
reg7 = opmask_register| 7
reg8 = opmask_register| 8
reg9 = opmask_register| 9
reg10 = opmask_register|10
reg11 = opmask_register|11
reg12 = opmask_register|12
reg13 = opmask_register|13
reg14 = opmask_register|14
reg15 = opmask_register|15
reg16 = opmask_register|16
reg17 = opmask_register|17
reg18 = opmask_register|18
reg19 = opmask_register|19
reg20 = opmask_register|20
reg21 = opmask_register|21
reg22 = opmask_register|22
reg23 = opmask_register|23
reg24 = opmask_register|24
reg25 = opmask_register|25
reg26 = opmask_register|26
reg27 = opmask_register|27
reg28 = opmask_register|28
reg29 = opmask_register|29
reg30 = opmask_register|30
reg31 = opmask_register|31
reg32 = opmask_register|32
reg33 = opmask_register|33
reg34 = opmask_register|34
reg35 = opmask_register|35
reg36 = opmask_register|36
reg37 = opmask_register|37
reg38 = opmask_register|38
reg39 = opmask_register|39
reg40 = opmask_register|40
reg41 = opmask_register|41
reg42 = opmask_register|42
reg43 = opmask_register|43
reg44 = opmask_register|44
reg45 = opmask_register|45
reg46 = opmask_register|46
reg47 = opmask_register|47
reg48 = opmask_register|48
reg49 = opmask_register|49
reg50 = opmask_register|50
reg51 = opmask_register|51
reg52 = opmask_register|52
reg53 = opmask_register|53
reg54 = opmask_register|54
reg55 = opmask_register|55
reg56 = opmask_register|56
reg57 = opmask_register|57
reg58 = opmask_register|58
reg59 = opmask_register|59
reg60 = opmask_register|60
reg61 = opmask_register|61
reg62 = opmask_register|62
reg63 = opmask_register|63
reg64 = opmask_register|64
reg65 = opmask_register|65
reg66 = opmask_register|66
reg67 = opmask_register|67
reg68 = opmask_register|68
reg69 = opmask_register|69
reg70 = opmask_register|70
reg71 = opmask_register|71
reg72 = opmask_register|72
reg73 = opmask_register|73
reg74 = opmask_register|74
reg75 = opmask_register|75
reg76 = opmask_register|76
reg77 = opmask_register|77
reg78 = opmask_register|78
reg79 = opmask_register|79
reg80 = opmask_register|80
reg81 = opmask_register|81
reg82 = opmask_register|82
reg83 = opmask_register|83
reg84 = opmask_register|84
reg85 = opmask_register|85
reg86 = opmask_register|86
reg87 = opmask_register|87
reg88 = opmask_register|88
reg89 = opmask_register|89
reg90 = opmask_register|90
reg91 = opmask_register|91
reg92 = opmask_register|92
reg93 = opmask_register|93
reg94 = opmask_register|94
reg95 = opmask_register|95
reg96 = opmask_register|96
reg97 = opmask_register|97
reg98 = opmask_register|98
reg99 = opmask_register|99
reg100 = opmask_register|100
reg101 = opmask_register|101
reg102 = opmask_register|102
reg103 = opmask_register|103
reg104 = opmask_register|104
reg105 = opmask_register|105
reg106 = opmask_register|106
reg107 = opmask_register|107
reg108 = opmask_register|108
reg109 = opmask_register|109
reg110 = opmask_register|110
reg111 = opmask_register|111
reg112 = opmask_register|112
reg113 = opmask_register|113
reg114 = opmask_register|114
reg115 = opmask_register|115
reg116 = opmask_register|116
reg117 = opmask_register|117
reg118 = opmask_register|118
reg119 = opmask_register|119
reg120 = opmask_register|120
reg121 = opmask_register|121
reg122 = opmask_register|122
reg123 = opmask_register|123
reg124 = opmask_register|124
reg125 = opmask_register|125
reg126 = opmask_register|126
reg127 = opmask_register|127

spf_all_teams_are_enemy                      = 0x00000001
spf_is_horseman                              = 0x00000002
spf_examine_all_spawn_points                 = 0x00000004
spf_team_0_spawn_far_from_entry_32           = 0x00000008
spf_team_1_spawn_far_from_entry_0            = 0x00000010
spf_team_1_spawn_far_from_entry_66           = 0x00000020
spf_team_0_spawn_near_entry_0                = 0x00000040
spf_team_0_spawn_near_entry_66               = 0x00000080
spf_team_1_spawn_near_entry_32               = 0x00000100
spf_team_0_walkers_spawn_at_high_points      = 0x00000200
spf_team_1_walkers_spawn_at_high_points      = 0x00000400
spf_try_to_spawn_close_to_at_least_one_enemy = 0x00000800
spf_care_agent_to_agent_distances_less       = 0x00001000
