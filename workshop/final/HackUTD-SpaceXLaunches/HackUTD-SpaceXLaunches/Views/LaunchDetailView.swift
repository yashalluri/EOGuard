//
//  LaunchDetailView.swift
//  HackUTD-SpaceXLaunches
//
//  Created by Nihaal Manesia on 11/11/24.
//

import SwiftUI

struct LaunchDetailView: View {
    let launch: Launch
    let possibleEmoji = ["🚀", "🛰️", "🧑‍🚀", "🔭", "🪐", "☄️", "🌕", "🌑"]
    
    var body: some View {
        ScrollView {
            Text(possibleEmoji.randomElement() ?? "🚀")
                .font(.system(size: 150))
                .padding(.vertical)
            HStack {
                Text("Date of Launch")
                    .bold()
                Spacer()
                Text(launch.dateUnix.toString())
            }
            .padding(.horizontal)
            HStack {
                Text("Flight Number")
                    .bold()
                Spacer()
                Text("\(launch.flightNumber)")
            }
            .padding(.horizontal)
            if let success = launch.success {
                HStack {
                    Text("Was the launch a success?")
                        .bold()
                    Spacer()
                    Text(success ? "Yes" : "No")
                        .foregroundStyle(success ? .green : .red)
                }
                .padding(.horizontal)
            }
            if let details = launch.details {
                Text(details)
                    .padding(.top)
                    .padding(.horizontal)
            }
        }
        .scrollBounceBehavior(.basedOnSize)
        .navigationTitle(launch.name)
    }
}

#Preview {
    let previewLaunch = Launch(flightNumber: 1, name: "First Launch", dateUnix: Date(), details: nil, success: false)
    return LaunchDetailView(launch: previewLaunch)
}
