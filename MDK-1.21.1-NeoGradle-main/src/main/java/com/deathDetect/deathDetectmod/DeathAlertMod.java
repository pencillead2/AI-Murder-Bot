package com.yourname.deathalertmod;

import net.neoforged.fml.common.Mod;
import net.neoforged.fml.event.lifecycle.FMLCommonSetupEvent;
import net.neoforged.fml.javafmlmod.FMLJavaModLoadingContext;

@Mod(DeathAlertMod.MODID)
public class DeathAlertMod {
    public static final String MODID = "deathalertmod";

    public DeathAlertMod() {
        FMLJavaModLoadingContext.get().getModEventBus().addListener(this::onCommonSetup);
    }

    private void onCommonSetup(final FMLCommonSetupEvent event) {
        System.out.println("Death Alert Mod loaded!");
    }
}
