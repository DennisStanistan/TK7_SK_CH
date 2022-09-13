# Contains operators used for the panel (TK_PT.py) and relies on the functions from TK_FX.py
#bl_idname should all be in lowercase for blender 2.8->3.1
#Dev note: Had a really weird issue where I was able to access TK_PROP_FX through TK_PROP 

# from re import T
import bpy
# import random
from bpy.types import Operator#,PropertyGroup, UIList, Panel

from.TK_FX import *
# from.TK_PROP import *
from.TK_PROP_FX import *
# from.TK_UI import *

class SK_CH_BlenderScene(Operator):
    """Clears out all objects and adjusts the scene settings for character meshes"""
    bl_idname = "object.tk7_scene_setup"
    bl_label = "Scene setup"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        # obj = context.active_object

        # # if obj is not None:
        # if obj.mode == 'OBJECT':
        return True

    def execute(self, context):
        TekkenSceneSetup()
        return {'FINISHED'}
   
    
class SK_CH_Export(Operator):
    """Applies the correct export settings for character meshes"""
    bl_idname = "object.tk7_export"
    bl_label = "Character Export"
    # bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        Objs = [object for object in bpy.data.objects if (object.type == 'ARMATURE')]

        
        if obj is not None:
            if obj.type == 'ARMATURE' and len(Objs)==1:
                if obj.mode == 'OBJECT':
                    if bpy.data.filepath != '':
                        return True
        

        return False

    def execute(self, context):
        TekkenFBXexporter()
        return {'FINISHED'}



class SK_CH_Test(Operator):
    """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
    bl_idname = "object.sk_test"
    bl_label = "Test functions"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT':
                # if obj.mode == 'EDIT':
                    if len(context.selected_objects)==1:
                        return True
        

        return False


    # def poll(cls, context): #Skeleton pose mode poll
    #     obj = context.active_object

    #     if obj is not None:
    #         if obj.type == 'ARMATURE':
    #             if obj.mode == 'POSE':
    #                 return True
        

    #     return False


    def execute(self, context):
        Test()
        # BoneMergeActive()
        # Simplifier()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}






class SK_CH_ApplyPose(Operator):
    """Applies the pose of the current active skeleton"""
    bl_idname = "object.sk_applypose"
    bl_label = "Apply pose"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT'or obj.mode == 'POSE':
                    return True
        

        return False


    def execute(self, context):
        # Simplifier()
        ApplyPose()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}


class SK_CH_Tposer(Operator):
    """T-poses the current active skeleton according Tekken 7's bone naming convention"""
    bl_idname = "object.sk_tposer"
    bl_label = "T-Poser"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT':
                    if len(context.selected_objects)==1:
                        return True
        

        return False


    def execute(self, context):
        # Simplifier()
        T_Poser(context.scene.tp_fix_armature, context.scene.tp_fix_fingertips, context.scene.tp_tpose_spine)
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}



class SK_CH_Pose_Snapper(Operator):
    """Snaps the bones in pose mode to align the bone positions of the active armature with another selected armature following Tekken 7's bone naming convention"""
    bl_idname = "object.sk_pose_snapper"
    bl_label = "Pose Snapper"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT':
                    if len(context.selected_objects)==2:
                        return True
        

        return False


    def execute(self, context):
        # Simplifier()
        Pose_Snapper(context.scene.ps_autoscale, context.scene.ps_mode_enum)
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}


class SK_CH_BoneFix(Operator):
    """Matches the active skeleton with the selected skeleton in edit mode and adds a few main bones if needed"""
    bl_idname = "object.sk_bonefix"
    bl_label = "Fix bones"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT' or obj.mode == 'EDIT':
                    if len(context.selected_objects)==2:
                        return True
        

        return False


    def execute(self, context):
        # Simplifier()
        ArmatureMatchFixer()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}

#Both mergers were merged (HA)
# class SK_CH_BoneMergeActive(Operator):
#     """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
#     bl_idname = "object.sk_bonemergeactive"
#     bl_label = "Test functions"

#     @classmethod
#     def poll(cls, context): #Skeleton edit mode poll for one selected object
#         obj = context.active_object

#         if obj is not None:
#             if obj.type == 'ARMATURE':
#                 if obj.mode == 'EDIT':
#                     if len(context.selected_objects)==1:
#                         return True
        

#         return False


#     def execute(self, context):
#         BoneMergeActive()
#         # Simplifier()
#         # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
#         return {'FINISHED'}


# class SK_CH_BoneMergeParent(Operator):
#     """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
#     bl_idname = "object.sk_bonemergeparent"
#     bl_label = "Test functions"

#     @classmethod
#     def poll(cls, context): #Skeleton edit mode poll for one selected object
#         obj = context.active_object

#         if obj is not None:
#             if obj.type == 'ARMATURE':
#                 if obj.mode == 'EDIT':
#                     # if len(context.selected_objects)==1:
#                     return True
        

#         return False


#     def execute(self, context):
#         BoneMergeParent()
#         # Simplifier()
#         # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
#         return {'FINISHED'}



class SK_CH_BoneMerge(Operator):
    """Merges the selected bones and merges their weights either to their parents or to the active bone (last selected bone) """
    bl_idname = "object.sk_bonemerger"
    bl_label = "Bone Merger"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'EDIT':
                    if len(context.selected_objects)==1:
                        if (context.scene.Bone_Mrg_enum == '1' and len(context.selected_bones)>1) or (context.scene.Bone_Mrg_enum == '0' and len(context.selected_bones)!=0):
                            return True
        

        return False


    def execute(self, context):
        if context.scene.Bone_Mrg_enum == '0':
            print("parent")
            BoneMergeParent()
        elif context.scene.Bone_Mrg_enum == '1':
            print("active")
            BoneMergeActive()
        # Simplifier()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}





#Moved to the renamer portion down below (might be/become outdated)
# class SK_CH_BoneRenamer(Operator):
#     """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
#     bl_idname = "object.sk_bonerename"
#     bl_label = "Test functions"

#     @classmethod
#     def poll(cls, context): #Skeleton edit mode poll for one selected object
#         obj = context.active_object

#         if obj is not None:
#             if obj.type == 'ARMATURE':
#                 if obj.mode == 'OBJECT':
#                     # if len(context.selected_objects)==2:
#                     return True
        

#         return False


#     def execute(self, context):
#         # Test()
#         Renamer()
#         # Simplifier()
#         # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
#         return {'FINISHED'}


class SK_CH_BoneRemove(Operator):
    """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
    bl_idname = "object.sk_bnremove"
    bl_label = "Test functions"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT':
                # if obj.mode == 'EDIT':
                    if len(context.selected_objects)==1:
                        return True
        

        return False


    def execute(self, context):
        BnRemover()

        return {'FINISHED'}

class SK_CH_PosMove(Operator):
    """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
    bl_idname = "object.sk_posmove"
    bl_label = "Test functions"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT' or obj.mode == 'POSE':
                    if len(context.selected_objects)==2:
                        return True
        

        return False


    def execute(self, context):
        # Test()
        BonPosMove()
        # Simplifier()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}


#______________________SK Generator_____________________
class SK_CH_SK_Generator(Operator):
    """Generates the skeleton for a Tekken character that works in Tekken 7"""
    bl_idname = "object.tk7_sk_generator"
    bl_label = "Generate Skeleton"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj is None or (obj is not None and obj.mode == 'OBJECT'):
        # if obj.mode == 'OBJECT':
            return True

    def execute(self, context):

        SK_Gen(context.scene.sk_gen_char_enum, context.scene.sk_gen_opt1_enum, context.scene.sk_gen_opt2_enum )
        # TekkenSceneSetup()
        return {'FINISHED'}



#______________Bone renamer list_________________________

class Bone_Renamer_Preset_Load_Operator(bpy.types.Operator):
    """Loads the stored preset files."""
    bl_idname = "bone_renamer_preset.load"
    bl_label = "Load"
    # bl_options = {'REGISTER', 'UNDO'}
    

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        PresetNames = Find_File_Names('Rename_Presets', ".txt")
        if not CheckPresetNameMatch():
        # if len(PresetNames) != len(context.scene.preset_collection) or not CheckPresetNameMatch():
            return True

    def execute(self, context):
        
        InitializeBoneRenamerEnumerator()
        # bpy.context.scene.preset_enum   = '0'

        return {'FINISHED'}



class Bone_Renamer_Preset_Add_Operator(bpy.types.Operator):
    """Add an entire new renaming list."""
    bl_idname = "bone_renamer_preset.add"
    bl_label = "Add bone renamer preset"
    # bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        PresetNames = Find_File_Names('Rename_Presets', ".txt")
        # if len(PresetNames) == len(context.scene.preset_collection):
        if CheckPresetNameMatch():
            return True

    def execute(self, context):
        
        Test_Number = context.scene.preset_collection.add()
        # Test_Number.number = random.randint(1, 4)

        Number = len(context.scene.preset_collection)-1
        bpy.context.scene.preset_enum = str(Number)

        Test_Number.RenameListPreset = "New"

        FillNewPreset()

        return {'FINISHED'}


class Bone_Renamer_Preset_Remove_Operator(bpy.types.Operator):
    """Remove an entire renaming list."""
    bl_idname = "bone_renamer_preset.remove"
    bl_label = "Remove bone renamer preset"
    # bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        if context.scene.preset_enum   != '' and CheckPresetNameMatch():
            return True


    def execute(self, context):
        
        if len(context.scene.preset_collection) > 0 and bpy.context.scene.preset_enum != '':
            FileRemover('Rename_Presets' ,context.scene.preset_collection[int(bpy.context.scene.preset_enum)].RenameListPreset)
            context.scene.preset_collection.remove(int(bpy.context.scene.preset_enum))
            ClearBoneRenameList()
            if bpy.context.scene.preset_enum == '0' and len(context.scene.preset_collection) > 0:
                bpy.context.scene.preset_enum = '0'


        return {'FINISHED'}


#Test Operators for lists
class LIST_OT_BoneRename_NewItem(Operator):
    """Add a new bone rename line to the list."""

    bl_idname = "bone_rename_list.new_item"
    bl_label = "Add a new bone rename line"

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        if context.scene.preset_enum   != '' and CheckPresetNameMatch():
            return True

    def execute(self, context):
        context.scene.bone_rename_list.add()
        my_list = context.scene.bone_rename_list
        context.scene.bone_rename_list_index = len(my_list)-1

        # Path = 'Rename_Presets/'+ context.scene.preset_collection[int(context.scene.preset_enum)].RenameListPreset +'.txt'
        # SaveBoneRenameList(Path, my_list)

        return{'FINISHED'}

class LIST_OT_BoneRename_DeleteItem(Operator):
    """Delete the selected bone rename line from the list."""

    bl_idname = "bone_rename_list.delete_item"
    bl_label = "Deletes bone rename line"
    # bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if context.scene.preset_enum   != '' and CheckPresetNameMatch():
            return True

    def execute(self, context):
        my_list = context.scene.bone_rename_list
        index = context.scene.bone_rename_list_index

        my_list.remove(index)
        context.scene.bone_rename_list_index = min(max(0, index - 1), len(my_list) - 1)


        Path = 'Rename_Presets/'+ context.scene.preset_collection[int(context.scene.preset_enum)].RenameListPreset +'.txt'
        SaveBoneRenameList(Path, my_list)

        return{'FINISHED'}

# class LIST_OT_MoveItem(Operator):
#     """Move an item in the list."""

#     bl_idname = "my_list.move_item"
#     bl_label = "Move an item in the list"

#     direction: bpy.props.EnumProperty(items=(('UP', 'Up', ""),
#                                               ('DOWN', 'Down', ""),))

#     @classmethod
#     def poll(cls, context):
#         return context.scene.my_list

#     def move_index(self):
#         """ Move index of an item render queue while clamping it. """

#         index = bpy.context.scene.list_index
#         list_length = len(bpy.context.scene.my_list) - 1  # (index starts at 0)
#         new_index = index + (-1 if self.direction == 'UP' else 1)

#         bpy.context.scene.list_index = max(0, min(new_index, list_length))

#     def execute(self, context):
#         my_list = context.scene.my_list
#         index = context.scene.list_index

#         neighbor = index + (-1 if self.direction == 'UP' else 1)
#         my_list.move(neighbor, index)
#         self.move_index()

#         return{'FINISHED'}






class SK_CH_BoneRenamer(Operator):
    """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
    bl_idname = "object.sk_bonerename"
    bl_label = "Test functions"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        obj = context.active_object

        if obj is not None and obj in bpy.context.selected_objects:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT':
                    if context.scene.preset_enum   != '' and CheckPresetNameMatch():
                    # if len(context.selected_objects)==2:
                        return True
        

        return False


    def execute(self, context):
        # Test()
        Renamer()
        # Simplifier()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}



class SK_CH_BoneRenamerListPopulate(Operator):
    """Auto populates the rename list based on the selected skeleton's structure as long as the skeleton type is supported"""
    bl_idname = "bone_rename_list.populate"
    bl_label = "Auto bone matching"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context): #Skeleton edit mode poll for one selected object
        obj = context.active_object

        if obj is not None and obj in bpy.context.selected_objects:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT':
                    if context.scene.preset_enum   != '' and CheckPresetNameMatch():
                    # if len(context.selected_objects)==2:
                        return True
        

        return False


    def execute(self, context):
        # Test()
        RenamerListPopulate()
        # Simplifier()
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}



#____________________Simplifier_________________________


class LIST_OT_Substrng_NewItem(Operator):
    """Add a new item to the list."""

    bl_idname = "bone_substrng_list.new_item"
    bl_label = "Add a new item"
    # bl_options = {'REGISTER', 'UNDO'}

    # @classmethod
    # def poll(cls, context): #Skeleton edit mode poll for one selected object
    #     if context.scene.preset_enum   != '':
    #         return True

    def execute(self, context):
        context.scene.bone_substrng_list.add()
        indx = len(context.scene.bone_substrng_list)
        context.scene.bone_substrng_list_index = indx - 1
        # my_list = context.scene.bone_rename_list

        # Path = 'Rename_Presets/'+ context.scene.preset_collection[int(context.scene.preset_enum)].RenameListPreset +'.txt'
        # SaveBoneRenameList(Path, my_list)

        return{'FINISHED'}

class LIST_OT_Substrng_DeleteItem(Operator):
    """Delete the selected item from the list."""

    bl_idname = "bone_substrng_list.delete_item"
    bl_label = "Deletes an item"
    # bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene.bone_substrng_list

    def execute(self, context):
        my_list = context.scene.bone_substrng_list
        index = context.scene.bone_substrng_list_index 

        my_list.remove(index)
        context.scene.bone_substrng_list_index = min(max(0, index - 1), len(my_list) - 1)


        # Path = 'Rename_Presets/'+ context.scene.preset_collection[int(context.scene.preset_enum)].RenameListPreset +'.txt'
        # SaveBoneRenameList(Path, my_list)

        return{'FINISHED'}

class SK_CH_Simplify(Operator):
    """Moves auxiliary bones to other layers and enlarges primary bones without affecting how the mesh loads inside Tekken"""
    bl_idname = "object.sk_simplify"
    bl_label = "Merges bones and adjusts the skeleton"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object

        if obj is not None:
            if obj.type == 'ARMATURE':
                if obj.mode == 'OBJECT' or obj.mode == 'EDIT':
                    return True
        

        return False


    def execute(self, context):
        # Simplifier()
        BoneSubstrgList = GetBoneSubstringList()
        if BoneSubstrgList == []:
            Simplifier(PrsvBones = bpy.context.scene.bone_prsv, Removebones = bpy.context.scene.bone_remv, MergeMeshes =  bpy.context.scene.mesh_join, Remove_Trans = bpy.context.scene.clr_trnspc)
        else:
            Simplifier(PrsvBones = bpy.context.scene.bone_prsv, BoneSubstrgList = BoneSubstrgList, Removebones = bpy.context.scene.bone_remv, MergeMeshes =  bpy.context.scene.mesh_join, Remove_Trans = bpy.context.scene.clr_trnspc)
        # bpy.ops.wm.simplifier('INVOKE_DEFAULT') #ops followed by bl_idname to invoke it
        return {'FINISHED'}