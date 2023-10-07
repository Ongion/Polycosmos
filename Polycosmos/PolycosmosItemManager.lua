ModUtil.Mod.Register( "PolycosmosItemManager" )


local ItemsDataArray=
{
    "Darkness",
    "Keys",
}

-------------------- Auxiliary function for checking if a item is a filler item
function PolycosmosItemManager.IsFillerItem(string)
    return PolycosmosEvents.HasValue(ItemsDataArray, string)
end

--------------------

function PolycosmosItemManager.GiveFillerItem(item)
    if (item == "Keys") then
        GameState.Resources.LockKeys = GameState.Resources.LockKeys + 15
        print("THIS SHOULD GIVE 15 KEYS")
        if (GameState.Resources.LockKeys) then
            GameState.Resources.LockKeys = GameState.Resources.LockKeys + 15
        else
            GameState.Resources.LockKeys = 15
        end
    end
    if (item == "Darkness") then
        if (GameState.Resources.MetaPoints) then
            GameState.Resources.MetaPoints = GameState.Resources.MetaPoints + 500
        else
            GameState.Resources.MetaPoints = 500
        end
        print("THIS SHOULD GIVE 500 Darkness")
    end
end