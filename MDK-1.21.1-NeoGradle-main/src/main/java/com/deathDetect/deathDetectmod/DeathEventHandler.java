package com.yourname.deathalertmod;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.damagesource.DamageSource;
import net.neoforged.neoforge.event.entity.living.LivingDeathEvent;
import net.neoforged.neoforge.eventbus.api.SubscribeEvent;
import net.neoforged.neoforge.common.MinecraftForge;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;

public class DeathEventHandler {

    public DeathEventHandler() {
        MinecraftForge.EVENT_BUS.register(this);
    }

    @SubscribeEvent
    public void onPlayerDeath(LivingDeathEvent event) {
        LivingEntity entity = event.getEntity();
        if (entity instanceof ServerPlayer player) {
            String message = "Player died: " + player.getName().getString() + " at " + LocalDateTime.now();
            System.out.println(message);
            writeToFile(message);
        }
    }

    private void writeToFile(String message) {
        try {
            FileWriter writer = new FileWriter("death_alert.txt", false);
            writer.write(message);
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
